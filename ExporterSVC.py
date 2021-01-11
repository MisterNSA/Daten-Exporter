import time
import random
from pathlib import Path

import servicemanager
import win32event
import win32service
from SMWinservice import SMWinservice



class DatenExporterSVC(SMWinservice):
    _svc_name_ = "DatenExporterSVC"
    _svc_display_name_ = "Daten Exporter Service"
    _svc_description_ = "Der Datenexporter überwacht einen Ordner auf eintreffende Dateien und verschiebt diese in ein Zielverzeichnis."

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                        servicemanager.PYS_SERVICE_STARTED,
                        (self._svc_name_, ''))
        while self.isrunning:
            random.seed()
            x = random.randint(1, 1000000)
            Path(f'c:{x}.txt').touch()
            time.sleep(5)

if __name__ == '__main__':
    DatenExporterSVC.parse_command_line()
