# Funktionlibrary for the Exporter
# Creator: MisterNSA aka Tobias Dominik Weber
# Date: 03.09.2020 Version 1.0.0

import os

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

def getTime():
    from datetime import datetime
    now = datetime.now()
    # Extract Date and Time
    return now.strftime("%Y.%m.%d - %H:%M:%S")

