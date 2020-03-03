import shutil
import os
import Export_functions

def main():
    try:
        Sourcefolder = "C:/Users/Tobias/Desktop/import/"    # Sourcefolder
        Sourcefolder = Sourcefolder.lstrip('\u202a')

        Destfolder = '‪C:/Users/Tobias/Desktop/exportiert/'  # Destination Folder
        Destfolder = Destfolder.lstrip('\u202a')

        for filename in os.listdir(Sourcefolder): # Jede Datei einzeln nacheinander abrufen 
            Filesource = Sourcefolder + filename
            if Export_functions.access(Filesource) == True:         # testen, ob man exklusiven Zugriff hat

                shutil.copy((Filesource), (Destfolder) + (filename))   # Datei kopieren
                os.remove((Sourcefolder) + (filename))                                # Alte Datei löschen
            else:
                return
    except FileNotFoundError: #später mail mit warnung verschicken
        print('Das Verzeichnis, das es abzuarbeiten gilt, wird nicht gefunden. Die Verarbeitung wird deshalb abgebrochen !')
        input ('BITTE TASTE DRÜCKEN ZUM PROGRAMM BEENDEN!')       


if __name__ == "__main__":
    main()