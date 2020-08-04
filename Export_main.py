#*******************************************************************************************************************#
# A Servie that checks if a folder contains files and moves them to a specifig folder, depending on the filetype    #
# Creator: MisterNSA aka Tobias Dominik Weber                                                                       #
# Date: 03.08.2020 Version 0.7                                                                                      #
#-------------------------------------------------------------------------------------------------------------------#

import shutil
import os
import sys
import Export_functions as func
import time
import configparser 


def checkSettings():
    try:
        # Extract the Settings from the exporter_config.txt File
        config = configparser.ConfigParser()
        configfilepath = "exporter_config.txt"
        config.read(configfilepath)

        # Parse Paths
        Pfade_config = config["Pfade"]
        source = Pfade_config.get("Quellpfad")
        destination = Pfade_config.get("Zielpfad")
        wrong_destination = Pfade_config.get("Zielpfad, falls falscher Dateityp")

        # Parse the Timer
        Timer_config = config["Timer"]
        wait = int(Timer_config.get("Wartezeit in Sekunden"))

        # Parse the Datatype
        Datentyp_config = config["Datentypen"]
        fileType = Datentyp_config["Endug des Dateityps"]
            
        main(source, destination, wait, wrong_destination, fileType)
            
    except: # create new config.txt
        file = open("exporter_config.txt", "w")
        file.write("""[Pfade]
Quellpfad = 
Zielpfad = 
Zielpfad, falls falscher Dateityp = 
[Timer]
Wartezeit in Sekunden = 
[Datentypen]
Endug des Dateityps = .pdf""")
        file.close()
        sys.exit(0)


def main(source, destination, wait, wrong_destination, fileType):
    try:
        for filename in os.listdir(source): 
            filesource = source + filename
            if func.access(filesource) == True: # check if the file exists and isnt opened
                if func.isType(filename, fileType) == True: # check if the File has the right type
                    shutil.move(filesource, destination)
                else:
                    shutil.move(filesource, wrong_destination)

            else:
                continue
    except FileNotFoundError: # send Mail with Error 
        pass
        #func.mail() #WIP

    except: # In Case of another error
        pass # Add another Errormessage and send it per mail
    
    time.sleep(wait) #Wait x Seconds, befor a new loop
    checkSettings()


if __name__ == "__main__":
    checkSettings()




