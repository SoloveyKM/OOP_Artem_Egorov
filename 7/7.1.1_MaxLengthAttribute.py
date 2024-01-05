class MaxLengthAttribute:

    def __get__(self, instance, owner):
        if instance.__dict__:
            return max(instance.__dict__, key=len)
        else:
            return None

class MyClass:
    max_length_attribute = MaxLengthAttribute()

if __name__ == '__main__':
    obj = MyClass()
    obj.name = "Vasiliy"
    obj.city = "Saint Peterburg"
    obj.country = "Rus"
    print(obj.max_length_attribute)
