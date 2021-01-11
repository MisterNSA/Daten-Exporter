# Vorbemerkung zur Umgebung
**- Python -**
Notwendig ist eine saubere Python installation, insbesondere auf dem Produktiv Zielsystem.
Am einfachsten wenn Python für alle Benutzer installiert wird also in C:\Program Files\Python3xxx

Der System Path variablen sollte C:\Program Files\Python3xxx 
und C:\Program Files\Python3xxxScripts hinzugefügt werden.

**- pywin32 -**
Dann mit 

    pip install pywin32 

natürlich als Administrator (bzw. über eine Konsole mit Administrator Zugriff) 
den Zugriff auf das Windows Betriebssystem hinzufügen. 

**- Sicherheit und Einschränkung -**
Wenn der Umgang mit unterschiedlichen Python Konfigurationen, dem zugehörigen Umgang mit
den dazu notwendigenm Pfaden und Zgriffsberechtigungen verstanden ist, sollte auf dem 
Zielsystem eine Einschränkung auf den Dienstausführenden Benutzer beschränken.  

# Commands zum Umgang mit den Python Scripts 
**-Service installieren über Admin Konsole !-**
python ExporterSVC.py install

**-Service updaten über Admin Konsole !-**
python ExporterSVC.py update

**-Service Stoppen über Admin Konsole !-**
net stop DatenExporterSVC

**-Service Stoppen  über Admin Konsole !-**
net start DatenExporterSVC

# Probleme

**- pywintypes3xxxx.dll nicht gefunden -**
Der Dienst lässt sich nicht starten und beenden. 

Die Datei pywintypes3xx.dll wobei x für die Python Version steht wird nicht im Verzeichnis
 C:\Program Files\Python3xx\Lib\site-packages\win32\ 
 gefunden. Die DLLs aus C:\Program Files\Python3xx\Lib\site-packages\pywin32_system32\ in den Ordner
  C:\Program Files\Python3xx\Lib\site-packages\win32\  kopieren


