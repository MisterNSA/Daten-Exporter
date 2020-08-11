#*******************************************************************************************************************#
# A Servie that checks if a folder contains files and moves them to a specifig folder, depending on the filetype    #
# Creator: MisterNSA aka Tobias Dominik Weber                                                                       #
# Date: 11.08.2020 Version 0.8.5                                                                                    #
#-------------------------------------------------------------------------------------------------------------------#

import shutil
import os
import sys
import Export_functions as func
import time
import configparser
from pathlib import Path


def checkSettings():
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
        fileType = Datentyp_config["Endug des Dateityps"]

        main(source, destination, wait, wrong_destination, fileType, duplicate_destination)

    except:  # create new config.txt
        file = open("exporter_config.txt", "w")
        file.write("""[Pfade]
Quellpfad = 
Zielpfad = 
Zielpfad, falls falscher Dateityp = 
Zielpfad, falls Datei schon existiert =
[Timer]
Wartezeit in Sekunden = 
[Datentypen]
Endug des Dateityps = .pdf""")
        file.close()
        func.mail("Entweder war die config leer, ein Dateipfad korrupiert oder die config wurde inkorrekt geändert. Es wurde eine neue config erstellt und der Diesnst beendet.")
        sys.exit(0)

# Main Loop - Checks what criterias the File meets and moves it to the corresponding path
def main(source, destination, wait, wrong_destination, fileType, duplicate_destination):
    try:
        for filename in os.listdir(source):
            # pathlib adds a String builder. Instead of "+", you can use "/"
            filesource = (source/filename)
            # check if the file exists and isnt opened
            if func.access(filesource) == True:
                # check if the File has the right type
                if func.isType(filename, fileType) == True:
                    # Check if file is a duplicate
                    if filename in os.listdir(destination):
                        shutil.move(filesource, (duplicate_destination/filename))
                    else:
                        shutil.move(filesource, (destination/filename))
                else:
                    if filename in os.listdir(wrong_destination):
                        print(duplicate_destination/filename)
                        shutil.move(filesource, (duplicate_destination/filename))
                    else:
                        shutil.move(filesource, (wrong_destination/filename))

            else:
                continue
    # If an error occured, send mail with error to user
    except FileNotFoundError:
        func.mail(
            "A File, that was in the Folder a Second ago, was not found. Someone seems to modify the Data.")

    except RuntimeError:
        func.mail(RuntimeError)

    time.sleep(wait)  # Wait x seconds, befor a new loop
    main(source, destination, wait, wrong_destination, fileType, duplicate_destination)


if __name__ == "__main__":
    checkSettings()

# Whatever happens, that ends the programm, inform the user
func.mail("The Programm stopped running!")
