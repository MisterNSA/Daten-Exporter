# Funktionlibrary for the Exporter
# Creator: Tobias Dominik Weber
# Date: 10.08.2020 Version 0.9.1


# check if the File matches the Type from the config
def isType(source, fileType):
    if fileType in source:
        return True
    else:
        return False


# check if the File exists and isnt open
def access(source):
    import os
    if os.path.exists(source):       
        try: # check if file is opened
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
    connectionObject = smtplib.SMTP("ccb-mail-12")
    # connect to SMTP
    connectionObject.ehlo()
    # Beginn Encryption
    connectionObject.starttls()
    # Login to your Account: USER | PW
    connectionObject.login("t.weber@ccb.local", "")
    # From, To, Subject \n\n Text
    connectionObject.sendmail("t.weber@ccb.de", "t.weber@ccb.de",
                              f"Subject: An Error Occured\n\n {now} \n {error_message} ")
    # Disconnect
    connectionObject.quit()


