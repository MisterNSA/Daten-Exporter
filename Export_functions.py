# Funktionlibrary for the Exporter
# Creator: MisterNSA aka Tobias Dominik Weber
# Date: 03.09.2020 Version 1.0.0

import os
from dotenv import load_dotenv

# load the Enviremental Variables from the .env file
load_dotenv()



def isType(source, fileType):
    """check if the File matches the Type from the config"""
    # If the are no endings in specified, every ending is valid
    if len(fileType) > 1:
        return True
    if any(ending in source for ending in fileType):
        return True
    else:
        return False

def Starts_with_Number(filename):
    """Check if the File starts with a number. Needed for assignment"""
    try:
        int(filename[0])
        return True
    except:
        return False

def access(source):
    """check if the File exists and isnt open"""
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


def mail(error_message):
    """sends a Mail with an error message to the user"""
    import smtplib
    # SMTP Server and Port
    connectionObject = smtplib.SMTP(os.getenv("SMTP_SERVER"))
    # connect to SMTP
    connectionObject.ehlo()
    # Beginn Encryption
    connectionObject.starttls()
    # Login to your Account: USER | PW
    connectionObject.login(os.getenv("ADDRESS_SENDER"), os.getenv("PASSWORD_SENDER"))
    # From, To, Subject \n\n Text
    connectionObject.sendmail(os.getenv("ADDRESS_SENDER"), os.getenv("ADDRESS_RECEIVER") ,
                              f"Subject: An Error Occured\n\n Datum: {getTime()} \n {error_message} ")
    # Disconnect
    connectionObject.quit()

def getTime():
    from datetime import datetime
    now = datetime.now()
    # Extract Date and Time
    return now.strftime("%Y.%m.%d - %H:%M:%S")

mail("Hilfe, es hat funktioniert")