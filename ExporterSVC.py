#****************************************************************************************************************************#
# A Windows Service that checks if a folder contains files and moves them to a specifig folder, depending on the filetype    #
# Creator: MisterNSA aka Tobias Dominik Weber                                                                                #
# Date: .09.2020 Version 1.0                                                                                                 #
# Changes: 12.01.2021, Frank Gottwald
# Implement Windows Service funtionality using piwin32
# Moving funtions to DatenExporterSVC Class
#----------------------------------------------------------------------------------------------------------------------------#

import sys
import shutil
import os
import time
import random
from pathlib import Path

import servicemanager
import win32event
import win32service
from SMWinservice import SMWinservice


import Export_functions as func
from dotenv import load_dotenv

import configparser


class DatenExporterSVC(SMWinservice):
    _svc_name_ = "DatenExporterSVC"
    _svc_display_name_ = "Daten Exporter Service"
    _svc_description_ = "Der Datenexporter überwacht einen Ordner auf eintreffende Dateien und verschiebt diese in ein Zielverzeichnis."

    

    def start(self):

            self.isrunning = True
       

    def stop(self):
        self.isrunning = False


    def checkSettings(self):
        """Reads the settings from the config file"""
        
        try:
            servicemanager.LogInfoMsg("Lese Konfiguration aus:")
            # Extract the Settings from the exporter_config.txt File
            config = configparser.ConfigParser()
            configfilepath = "c:/windows/exporter_config.ini"
            
            
            config.read(configfilepath)

            # Parse Paths
            Pfade_config = config["Pfade"]

            self.source : Path = Path(config["Pfade"]["Quellpfad"])
           
            self.source : Path = Path(Pfade_config.get("Quellpfad"))
            self.destination : Path = Path(Pfade_config.get("Zielpfad"))
            self.wrong_destination : Path = Path(Pfade_config.get("Zielpfad, falls falscher Dateityp"))
            self.duplicate_destination : Path = Path(Pfade_config.get("Zielpfad, falls Datei schon existiert"))
            
            # Parse the Timer
            Timer_config = config["Timer"]
            self.wait = int(Timer_config.get("Wartezeit in Sekunden"))



            # Parse the Datatype
            Datentyp_config = config["Datentypen"]
            self.fileType = Datentyp_config["Endungen des Dateityps"].split(", ")

            servicemanager.LogInfoMsg(os.getcwd())

            servicemanager.LogInfoMsg("source:" + str(self.source))
            servicemanager.LogInfoMsg("destination:" + str(self.destination))
            servicemanager.LogInfoMsg("wrong_destination:" + str(self.wrong_destination))
            servicemanager.LogInfoMsg("duplicate_destination:" + str(self.duplicate_destination))
            servicemanager.LogInfoMsg("wait:" + str(self.wait))
            servicemanager.LogInfoMsg("Endungen:" + str(self.fileType))

            # TODO: Prüfung ob die Pfade überhaupt da sind !



        except:  # create new config.txt
            servicemanager.LogInfoMsg("Schreibe neue Konfig nach c:\\windows\\exporter_config.ini:")

            # TODO: nich immer ist die Config nicht da, ggf. nur Fehlerhaft.

            with open(configfilepath, "w") as file:
                file.write("""[Pfade]
    Quellpfad = 
    Zielpfad = 
    Zielpfad, falls falscher Dateityp = 
    Zielpfad, falls Datei schon existiert = 
    [Timer]
    Wartezeit in Sekunden = 
    [Datentypen]
    Endungen des Dateityps = .pdf, .jpg, .png
    #Bitte alle Dateiendungen durch ein Komma gefolgt von einem Lehrzeichen trennen. Z.B.  .pdf, .jpg, .png""")

            func.mail("Entweder war die config leer, ein Dateipfad korrupiert oder die config wurde inkorrekt geaendert. Es wurde eine neue config erstellt und der Dienst beendet.")
        
            # Change from Exit to Raise Event, so that the Windows Service handle this, and enables shutting down.
            #sys.exit(0)
            raise RuntimeError("Irgendetwas ging schief / ist falsch in den Settings!")

    def main(self):
        
        
        load_dotenv()
        
        self.checkSettings()

        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                        servicemanager.PYS_SERVICE_STARTED,
                        (self._svc_name_, ''))

        while self.isrunning:

            servicemanager.LogInfoMsg("Into the main loop !")
            
            """Main Loop - Checks what criterias the File meets and moves it to the corresponding path"""
            
            try:
                for filename in os.listdir(self.source):
                    # pathlib adds a String builder. Instead of "+", you can use "/"
                    filesource = (self.source/filename)
                    # check if the file exists and isnt opened
                    if func.access(filesource) == True:
                        # check if the File has the right type and starts with a number
                        if func.isType(filename, self.fileType) and func.Starts_with_Number(filename):
                            # Check if file is a duplicate
                            if filename in os.listdir(self.destination):
                                shutil.move(filesource, (self.duplicate_destination/filename))
                            else:
                                shutil.move(filesource, (self.destination/filename))
                        else:
                            if filename in os.listdir(self.wrong_destination):
                                shutil.move(filesource, (self.duplicate_destination/filename))
                            else:
                                shutil.move(filesource, (self.wrong_destination/filename))

                    else:
                        continue
                        
            # If an error occured, send mail with error to user
            except FileNotFoundError:
                message = f"""Entweder wurde ein Pfad nicht richtig eingelesen oder eine Datei wurde waehrend der Bearbeitung verschoben, was aber unwahrscheinlich ist.\n
        Pfade:\n
        Quellpfad = {self.source}\n
        Zielpfad = {self.destination}\n
        Zielpfad, falls falscher Dateityp = {self.wrong_destination}\n
        Zielpfad, falls Datei schon existiert = {self.duplicate_destination}\n\n
        Wenn es Fehler in der Pfadangabe gibt, versuchen Sie bitte den Pfad in der config zu loeschen und per Hand neu einzutragen.\n
        Falls auch dies nichts bringt, loeschen sie bitte die config. Beim naechsten Programmstart wird automatisch eine neue config erstellt.
        """
                
                servicemanager.LogErrorMsg(message)

                func.mail(message)
                sys.exit(0)

            except RuntimeError:

                servicemanager.LogErrorMsg(RuntimeError)
                
                func.mail(RuntimeError)
                
                self.isrunning=False

                sys.exit(0)

            time.sleep(self.wait)  # Wait x seconds, befor a new loop


if __name__ == '__main__':
    DatenExporterSVC.parse_command_line()
