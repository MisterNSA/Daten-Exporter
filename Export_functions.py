#Funktionlibrary for the Exporter
#Creator: Tobias Dominik Weber
#Date: 15.06.2020 Versin 0.9


# check if the File matches the Type from the config
def isType(source, fileType):
    if fileType in source:
        return True
    else:
        return False 


# check if the File exists and isnt open 
def access(source): 
    import os
    if os.path.exists(source):       # check if File existiert
        try:                           # check if file is opened
            f = open(source, "w")    
            ergebnis = True            
            f.close() 
        except:
            ergebnis = False
        finally:
            return ergebnis


def mail():
    pass # WORK IN PROGRESS
    """
    import smtplib
    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEText import MIMEText

    senderEmail = "tobiasweber1029@googlemail.com"
    empfangsEmail = "tobiasweber1029@googlemail.com"
    msg = MIMEMultipart()
    msg["From"] = senderEmail
    msg["To"] = empfangsEmail
    msg["Subject"] = "Es ist ein Fehler aufgetreten"

    #emailText = "Das Programm wurde unerwartet beendet. Bitte neu starten!"
    #msg.attach(MIMEText(emailText, "html"))

    server = smtplib.SMTP("mail.google.net", 993) # Die Server Daten
    server.starttls()
    server.login(senderEmail, "tobiasdominiki") # Das Passwort
    text = msg.as_string()
    server.sendmail(senderEmail, empfangsEmail, text)
    server.quit()
    """
