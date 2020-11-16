# Daten-Exporter
Grundgerüst eines für meinen Betrieb erstellten Programms zum Überwachen eines Ordners. Daten werden nach bestimmten Merkmalen getrennt in unterschiedliche Verzeichnisse geschoben. 

# Funktionalitäten bisher
**-Ordner überwachen und Daten verschieben.**
Verschiedene Ziele, 
1. wenn die Datei konform ist, 
2. wenn die Datei eine falsche Endung hat,
3. wenn die Datei im Zielverzeichnis schon existiert

**-Bei Fehlern, Fehlermeldungen per Mail versenden** 

#Merkmale nach denen Geordnet werden kann

**Dateityp/ -endung**

# Inhalt der config
1. Quellpfad = Ordner, der überwacht werden soll
2. Zielpfad = Ordner, in den konforme Dateien verschoben werden sollen
3. Zielpfad, falls falscher Dateityp = Ordner, in den nicht konforme Dateien verschoben werden sollen
4. Zielpfad, falls Datei schon existiert = Ordner, in den Dateien verschoben werden sollen, die im Zielverzeichnis schon existieren

