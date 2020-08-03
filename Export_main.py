import shutil
import os
import Export_functions as func
import time


# Extract the Settings from the exporter_config.txt File
def checkSettings():
    counter = 0
    try:
        data_source = open("exporter_config.txt", "r") 
        for i in data_source:  
            counter += 1
            if counter == 1:
                source = i # source of Files
                source = source.lstrip("Quellpfad: â€ª ") #extract only valid Information
                source = source.strip()
            if counter == 2:
                destination = i # Destination for Files that match the format
                destination = destination.lstrip("Zielpfad: â€ª ") #extract only valid Information
                destination = destination.strip()
            if counter == 3:
                wrongDestination = i # Destination for Files that dont match the format
                wrongDestination = wrongDestination.lstrip("Zielpfad, falls falscher Dateityp: â€ª ") #extract only valid Information
                wrongDestination = wrongDestination.strip()
            if counter == 4:
                wait = i # Time to wait after each loop
                wait = int(wait.lstrip("Wartezeit in Sekunden: ")) #extract only valid time
            if counter == 5:
                fileType = i # The ending to check if the File has the right Type
                fileType = fileType.lstrip("Endug der gewünschten Dateityps: ") #extract only valid Information
                fileType = fileType.strip()
            if counter > 5:
                break
        data_source.close()
        main(source, destination, wait, wrongDestination, fileType)
            
    except FileNotFoundError: # create new config.txt
        file = open("exporter_config.txt", "w")
        file.write("Quellpfad: ")
        file.write("Zielpfad: ")
        file.write("Zielpfad, falls falscher Dateityp: ")
        file.write("Wartezeit in Sekunden: ")
        file.write("Endug des gewünschten Dateityps: " + "\n")
        file.write("""!WICHTIG!
Nach dem Doppelpunkt muss immer ein Zeichen Platz sein. 
Quell- und Zielpfad im folgenden Format angeben: C:/Users/Test/quelle/ oder C:/ziel/
Der Pfadname darf keine "\" enthalten und muss am Schluss ein "/" stehen haben
Die Wartezeit nur als Zahl angeben.
Die Endung im Format z.B: .pdf .py .exe .docx """)
        file.close()
        time.sleep(300) # wait 5 Minutes for the User to Input settings
        checkSettings()


def main(source, destination, wait, wrongDestination, fileType):
    try:
        for filename in os.listdir(source): 
            filesource = source + filename
            if func.access(filesource) == True: # check if the file exists and isnt opened
                if func.isType(filename, fileType) == True: # check if the File has the right type
                    shutil.move(filesource, destination)
                else:
                    shutil.move(filesource, wrongDestination)

            else:
                continue
    except FileNotFoundError: # send Mail with Error 
        func.mail() #WIP
    
    time.sleep(wait) #Wait x Seconds, befor a new loop
    checkSettings()


if __name__ == "__main__":
    checkSettings()




