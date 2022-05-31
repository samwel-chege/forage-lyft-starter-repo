from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine
from engine.battery.nubbin_battery.py import NubbinBattery

class Rorschach(WilloughbyEngine):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
