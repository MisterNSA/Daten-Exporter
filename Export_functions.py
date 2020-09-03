# Funktionlibrary for the Exporter
# Creator: Tobias Dominik Weber
# Date: 17.08.2020 Version 0.9.2

# check if the File matches the Type from the config
def isType(source, fileType):
    if any(ending in source for ending in fileType):
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


# sends a Mail with an error message to the user
def mail(error_message, Address_sender, Password_sender, Address_receiver, Smtp_server):
    import smtplib
    # SMTP Server and Port
    connectionObject = smtplib.SMTP(Smtp_server)
    # connect to SMTP
    connectionObject.ehlo()
    # Beginn Encryption
    connectionObject.starttls()
    # Login to your Account: USER | PW
    connectionObject.login(Address_sender, Password_sender)
    # From, To, Subject \n\n Text
    connectionObject.sendmail(Address_sender, Address_receiver,
                              f"Subject: An Error Occured\n\n Datum: {getTime()} \n {error_message} ")
    # Disconnect
    connectionObject.quit()

def getTime():
    from datetime import datetime
    now = datetime.now()
    # Extract Date and Time
    return now.strftime("%Y.%m.%d - %H:%M:%S")

