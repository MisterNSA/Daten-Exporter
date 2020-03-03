def access(Filesource):
    
    import os

    if os.path.exists(Filesource):       # testen ob Datei existiert

        try:                           # testen ob Datei geändert werden kann
            f = open(Filesource, "w")    
            ergebnis = True            
            f.close() 
            
        except:
            ergebnis = False

        finally:
            return (ergebnis)
