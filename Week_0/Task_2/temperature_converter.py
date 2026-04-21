
class TemperatureConverter:
    def __init__(self):
       
        # temperature 0 at the beginning
        self.__temperature = 0.0

    def setTemperature(self, temp: float) -> None:
        # user temparature
        self.__temperature = temp

    def toCelsius(self) -> float:
        
        return self.__temperature

    def toFahrenheit(self) -> float:
        # Celsius to Farhrenteit
        return (self.__temperature * 9 / 5) + 32

    def toKelvin(self) -> float:
        # Celsius to kelvin
        return self.__temperature + 273.15
