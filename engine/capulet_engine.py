from abc import ABC

from car import Car


class CapuletEngine(Car, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
      service_threshold_mileage = self.current_mileage - self.last_service_mileage
        if self.service_threshold_mileage > 30000:
            return True 
        else:
            return False
