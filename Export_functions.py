#Funktionsbibliothek für den Exporter
#Ersteller: Tobias Dominik Weber
#Datum: 01.04.2020 Versin 0.8

#nimmt Pfadname entgegen und gibt True zurück, wenn die Datei existiert und nicht beschrieben wird
def access(source): 
    
    import os

    if os.path.exists(source):       # testen ob Datei existiert

        try:                           # testen ob Datei geändert werden kann
            f = open(source, "w")    
            ergebnis = True            
            f.close() 
            
        except:
            ergebnis = False

        finally:
            return (ergebnis)


def mail():
    pass # Eingefügt, wenn ich es endlich zum laufen bekomme
    """
    import smtplib
    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEText import MIMEText

    senderEmail = "tobiasweber1029@googlemail.com"
    empfangsEmail = "tobiasweber1029@googlemail.com"
    msg = MIMEMultipart()
    msg['From'] = senderEmail
    msg['To'] = empfangsEmail
    msg['Subject'] = "Es ist ein Fehler aufgetreten"

    #emailText = "Das Programm wurde unerwartet beendet. Bitte neu starten!"
    #msg.attach(MIMEText(emailText, 'html'))

    server = smtplib.SMTP('mail.google.net', 993) # Die Server Daten
    server.starttls()
    server.login(senderEmail, "tobiasdominiki") # Das Passwort
    text = msg.as_string()
    server.sendmail(senderEmail, empfangsEmail, text)
    server.quit()
    """