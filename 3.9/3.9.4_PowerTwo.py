class PowerTwo:

    def __init__(self, degree):
        self.degree = degree

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index > self.degree:
            raise StopIteration
        value = pow(2, self.index)
        self.index += 1
        return value


if __name__ == '__main__':

    numbers = PowerTwo(2)

    assert hasattr(numbers, '__next__') is True
    assert hasattr(numbers, '__iter__') is True

    iterator = iter(numbers)
    print('Элементы итератора PowerTwo(2)')
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    try:
        print(next(iterator))
        raise ValueError('Не реализовали StopIteration')
    except StopIteration:
        pass

    print('-' * 15)
    print('Элементы итератора PowerTwo(20)')
    for i in PowerTwo(20):
        print(i)