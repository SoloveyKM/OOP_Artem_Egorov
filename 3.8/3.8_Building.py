class Building:

    def __init__(self, height):
        self.height = height
        self.floors = [None] * height

    def __getitem__(self, item):
        if 0 <= item < self.height:
            return self.floors[item]
        else:
            raise IndexError('индекс за границами')

    def __setitem__(self, key, value):
        if 0 <= key < self.height:
            self.floors[key] = value
        else:
            raise IndexError('индекс за границами')

    def __delitem__(self, key):
        if 0 <= key < self.height:
            self.floors[key] = None
        else:
            raise IndexError('индекс за границами')


if __name__ == '__main__':
    iron_building = Building(22)  # Создаем здание с 22 этажами
    iron_building[0] = 'Reception'
    iron_building[1] = 'Oscorp Industries'
    iron_building[2] = 'Stark Industries'
    print(iron_building[2])
    del iron_building[2]
    print(iron_building[2])