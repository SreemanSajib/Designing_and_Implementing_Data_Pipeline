
from dataclasses import dataclass

@dataclass
class SmartDevice:
    device_name: str
    status: str = "OFF"

    def operate(self):
        # Base method
        pass

@dataclass
class SmartLight(SmartDevice):
    
    brightness: int = 100

    def operate(self):
        self.status = "ON"
        print(f"SmartLight '{self.device_name}' is now {self.status} at {self.brightness}% brightness.")

@dataclass
class SmartThermostat(SmartDevice):
   
    temperature: int = 22

    def operate(self):
        self.status = "ACTIVE"
        print(f"SmartThermostat '{self.device_name}' is {self.status}. Setting temp to {self.temperature}°C.")

@dataclass
class SmartLock(SmartDevice):
    def operate(self):
        self.status = "LOCKED"
        print(f"SmartLock '{self.device_name}' status updated to: {self.status}.")
