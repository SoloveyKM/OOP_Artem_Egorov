class Celsius:

    def __init__(self, temperature):
        self.__temperature = temperature

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        if value >= -273.15:
            self.__temperature = value
        else:
            raise ValueError

    def to_fahrenheit(self):
        return self.__temperature * 9 / 5 + 32

if __name__ == '__main__':

    celsius = Celsius(25)
    assert celsius.temperature == 25
    assert celsius.to_fahrenheit() == 77.0

    celsius.temperature = 30
    assert celsius.temperature == 30
    assert celsius.to_fahrenheit() == 86.0

    print('Good')