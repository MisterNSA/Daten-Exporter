import shutil
import os
import Export_functions as func
import time

#kann keine Ordner kopieren

source = ""
destination = ""
wait = ""
counter = 0

Data_source = open('exporter_config.txt', 'r') #Nur die drei Angaben Quelle, Ziel und wartezeit einlesen
for i in Data_source:  
    counter += 1
    if counter == 1:
        source = i
    if counter == 2:
        destination = i 
    if counter == 3:
        wait = i
Data_source.close()

source = source.lstrip('Quellpfad: â€ª ') #Pfad zurechtschneiden
source = source.strip()

destination = destination.lstrip('Zielpfad: â€ª ') #Pfad zurechtschneiden
destination = destination.strip()


wait = int(wait.lstrip('Wartezeit in Sekunden: ')) #Auf Zeit reduzieren



def main(source, destination, wait):
    try:
        for filename in os.listdir(source): # Jede Datei einzeln nacheinander abrufen 
            Filesource = source + filename
            if func.access(Filesource) == True: # testen, ob die datei existiert und man exklusiven Zugriff hat

                shutil.copy((Filesource), (destination) + (filename)) # Datei kopieren
                os.remove((source) + (filename)) # Alte Datei löschen
            else:
                continue
    except FileNotFoundError: #später mail mit Warnung verschicken
        print('Das Verzeichnis, das es abzuarbeiten gilt, wird nicht gefunden. Die Verarbeitung wird deshalb abgebrochen!')
        #input ('BITTE TASTE DRÜCKEN ZUM PROGRAMM BEENDEN!')       
        func.mail() #WIP
    
    time.sleep(wait) #Wartet x Sekunden, bevor der Ordner wieder abgearbeitet wird
    main()


if __name__ == "__main__":
    main(source, destination, wait)

