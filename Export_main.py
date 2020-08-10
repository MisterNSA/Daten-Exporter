#*******************************************************************************************************************#
# A Servie that checks if a folder contains files and moves them to a specifig folder, depending on the filetype    #
# Creator: MisterNSA aka Tobias Dominik Weber                                                                       #
# Date: 10.08.2020 Version 0.8                                                                                      #
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
        wrong_destination = Pfade_config.get(
            "Zielpfad, falls falscher Dateityp")
        duplicate_destination = Pfade_config.get("Zielpfad, falls Datei schon existiert")

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
        sys.exit(0)

# Main Loop - Checks what criterias the File meets and moves it to the corresponding path
def main(source, destination, wait, wrong_destination, fileType, duplicate_destination):
    try:
        for filename in os.listdir(source):
            filesource = source + filename
            # check if the file exists and isnt opened
            if func.access(filesource) == True:
                # check if the File has the right type
                if func.isType(filename, fileType) == True:
                    # Check if file is a duplicate
                    if filename in os.listdir(destination):
                        shutil.move(filesource, duplicate_destination)
                    else:
                        shutil.move(filesource, destination)
                else:
                    if filename in os.listdir(wrong_destination):
                        shutil.move(filesource, duplicate_destination)
                    else:
                        shutil.move(filesource, wrong_destination)

            else:
                continue
    # If an error occured, send mail with error to user
    except FileNotFoundError:
        func.mail(
            "A File in the Folder was not found. Someone seems to modify the Data.")

    except RuntimeError:
        func.mail(RuntimeError)

    time.sleep(wait)  # Wait x seconds, befor a new loop
    main(source, destination, wait, wrong_destination, fileType, duplicate_destination)


if __name__ == "__main__":
    checkSettings()

# Whatever happens, that ends the programm, inform the user
func.mail("The Programm stopped running!")
