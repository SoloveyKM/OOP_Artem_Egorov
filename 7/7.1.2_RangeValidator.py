class RangeValidator:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def __set_name__(self, owner_class, attribute_name):
        self.attribute_name = attribute_name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.attribute_name]

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Неправильный тип данных')
        if value < self.min or value > self.max:
            raise ValueError(f'Значение должно быть между {self.min} и {self.max}')
        instance.__dict__[self.attribute_name] = value

class Temperature:
    celsius = RangeValidator(-273.15, 1000)
    kelvin = RangeValidator(0, 273)

if __name__ == '__main__':
    temp = Temperature()
    temp.celsius = -100
    print(temp.celsius)