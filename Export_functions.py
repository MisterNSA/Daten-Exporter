# Funktionlibrary for the Exporter
# Creator: Tobias Dominik Weber
# Date: 15.06.2020 Versin 0.9


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
            f = open(source, "a+")
            ergebnis = True
            f.close()
        except:
            ergebnis = False
        finally:
            return ergebnis


# sends a Mail with an error mesage to the user
def mail(error_message):
    import smtplib
    import datetime
    now = datetime.datetime.now()
    # SMTP Server and Port
    connectionObject = smtplib.SMTP("smtp.gmail.com", 587)
    # connect to SMTP
    connectionObject.ehlo()
    # Beginn Encryption
    connectionObject.starttls()
    # Login to your Account
    connectionObject.login('tobiasdominikweber@gmail.com', 'Tobias1029')
    # From, To, Subject \n\n Text
    connectionObject.sendmail("tobiasdominikweber@gmail.com", "tobiasdominikweber@gmail.com",
                              f"Subject: An Error Occured\n\n {now} \n {error_message} ")
    # Disconnect
    connectionObject.quit()

    # Maybe add: App Specific Passwort - Eigenes PW für Programme
