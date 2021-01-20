#*******************************************************************************************************************#
# A Servie that checks if a folder contains files and moves them to a specifig folder, depending on the filetype    #
# Creator: MisterNSA aka Tobias Dominik Weber                                                                       #
# Date: 03.09.2020 Version 1.0                                                                                      #
#-------------------------------------------------------------------------------------------------------------------#

import shutil
import os
import sys
import Export_functions as func
import time
import configparser
from pathlib import Path


def checkSettings():
    """Reads the settings from the config file"""
    try:
        # Extract the Settings from the exporter_config.txt File
        config = configparser.ConfigParser()
        configfilepath = "exporter_config.txt"
        config.read(configfilepath)

        # Parse Paths
        Pfade_config = config["Pfade"]
        source : Path = Path(Pfade_config.get("Quellpfad"))
        destination : Path = Path(Pfade_config.get("Zielpfad"))
        wrong_destination : Path = Path(Pfade_config.get("Zielpfad, falls falscher Dateityp"))
        duplicate_destination : Path = Path(Pfade_config.get("Zielpfad, falls Datei schon existiert"))

        # Parse the Timer
        Timer_config = config["Timer"]
        wait = int(Timer_config.get("Wartezeit in Sekunden"))

        # Parse the Datatype
        Datentyp_config = config["Datentypen"]
        fileType = Datentyp_config["Endungen des Dateityps"].split(", ")

    except:  # create new config.txt
        with open("exporter_config.txt", "w") as file:
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
        sys.exit(0)

    main(source, destination, wait, wrong_destination, fileType, duplicate_destination)


def main(source, destination, wait, wrong_destination, fileType, duplicate_destination):
    """Main Loop - Checks what criterias the File meets and moves it to the corresponding path"""
    try:
        for filename in os.listdir(source):
            # pathlib adds a String builder. Instead of "+", you can use "/"
            filesource = (source/filename)
            # check if the file exists and isnt opened
            try:
                # It seems like this only works if the File is not opened, so this is a test
                os.rename(filesource,filesource)
                # check if the File has the right type and starts with a number
                if func.isType(filename, fileType) and func.Starts_with_Number(filename):
                    # Check if file is a duplicate
                    if filename in os.listdir(destination):
                        shutil.move(filesource, (duplicate_destination/filename))
                    else:
                        shutil.move(filesource, (destination/filename))
                else:
                    if filename in os.listdir(wrong_destination):
                        shutil.move(filesource, (duplicate_destination/filename))
                    else:
                        shutil.move(filesource, (wrong_destination/filename))

            except:
                continue

    
    except FileNotFoundError:
        sys.exit(0)

    except RuntimeError:
        sys.exit(0)

    time.sleep(wait)  # Wait x seconds, befor a new loop
    main(source, destination, wait, wrong_destination, fileType, duplicate_destination)


if __name__ == "__main__":
    checkSettings()


