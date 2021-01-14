import sys
import time
import random
from pathlib import Path

import servicemanager
import win32event
import win32service
from SMWinservice import SMWinservice



class DatenExporterSVC(SMWinservice):
    _svc_name_ = "TestPythonSVC"
    _svc_display_name_ = "Test Python Service"
    _svc_description_ = "Der Test Python Service testet einen Dienst mit pywin32."

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                        servicemanager.PYS_SERVICE_STARTED,
                        (self._svc_name_, ''))
        message ="Jetzt wird es ernst :" + str(self.isrunning)
        servicemanager.LogInfoMsg(message)
        while self.isrunning:
            servicemanager.LogInfoMsg("In der Schleife !")
            try:
                random.seed()
                x = random.randint(1, 1000000)
                servicemanager.LogInfoMsg("Random ist :" + str(x))
                Path(f'c:\{x}.txt').touch()
                time.sleep(5)
            except:
                servicemanager.LogErrorMsg("Unbehandelter Fehler" + sys.exc_info()[0])

if __name__ == '__main__':
    DatenExporterSVC.parse_command_line()
