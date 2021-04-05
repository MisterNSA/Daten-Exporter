# Vorbemerkung zur Umgebung
**- Python -**
Notwendig ist eine saubere Python installation, insbesondere auf dem Produktiv Zielsystem.
Am einfachsten wenn Python mit allen Abhängigkeiten für alle Benutzer installiert wird 
also in C:\Program Files\Python3xxx

Der System Path variablen sollte C:\Program Files\Python3xxx 
und C:\Program Files\Python3xxxScripts hinzugefügt werden.

# Abhängigkeiten

**- Python 3.x - getestet mit 3.9 -**

**-- dotenv -**
pip install -U python-dotenv

**- pywin32 -**

pip install -U pywin32

natürlich als Administrator (bzw. über eine Konsole mit Administrator Zugriff) 
den Zugriff auf das Windows Betriebssystem hinzufügen. 

**- Sicherheit und Einschränkung -**
Wenn der Umgang mit unterschiedlichen Python Konfigurationen, dem zugehörigen Umgang mit
den dazu notwendigenm Pfaden und Zgriffsberechtigungen verstanden ist, sollte auf dem 
Zielsystem eine Einschränkung auf den Dienstausführenden Benutzer beschränken.  

# Commands zum Umgang mit den Python Scripts 

**- Administrator Console ! -**
Entweder ein CMD als Administrator ausführen 
oder Visual Studio Code als Administrator starten !

**-Service installieren über Admin Konsole !-**
python ExporterSVC.py install

**-Service updaten über Admin Konsole !-**
python ExporterSVC.py update

**-Service entfernen über Admin Konsole !-**
python ExporterSVC.py remove

**-Service debuggen über Admin Konsole !-**
python ExporterSVC.py debug

**-Service Stoppen über Admin Konsole !-**
net stop DatenExporterSVC

**-Service Starten über Admin Konsole !-**
net start DatenExporterSVC

# Probleme

**- pywintypes3xxxx.dll nicht gefunden -**
Der Dienst lässt sich nicht starten und beenden. 

Die Datei pywintypes3xx.dll wobei x für die Python Version steht wird nicht im Verzeichnis
 C:\Program Files\Python3xx\Lib\site-packages\win32\ 
 gefunden. Die DLLs aus C:\Program Files\Python3xx\Lib\site-packages\pywin32_system32\ in den Ordner
  C:\Program Files\Python3xx\Lib\site-packages\win32\  kopieren


# Konfiguration

**- exporter_config.ini -**

Die Datei wird beim Service in c:\windows\exporter_config.ini erwartet. 
CWD ist hier nämlich nicht der Pfad des aktuellen Scripts !!!!

# Known Bugs
    # TODO: Die Funktion "access" tut noch nicht genau das was sie tun soll !
    # es wird nicht verhindert das z.B. eine geöffnete Access Datenbank, also eine geöffnete Datei
    # eines anderen Prozesses, verschoben wird, und damit kommt es zu, Fehler !
    # Das sollte diese Funktion eigentlich überprüfen !!!

    # Ergebnis der Service crashed
