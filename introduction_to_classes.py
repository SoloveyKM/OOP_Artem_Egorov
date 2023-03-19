class Factory:
    pass


class Contact:
    name = 'Barak'
    phone_number = '+1 202 345 4564'


b = Contact()


class Book:
    name = '1984'
    writer = 'Джордж Оруэлл'
    pages = 213


class Cat:
    name = 'Матроскин'
    color = 'black'


class Empty:
    pass


my_list = [
    ('apple', 23),
    ('banana', 80),
    ('cherry', 13),
    ('date', 10),
    ('elderberry', 4),
    ('fig', 65),
    ('grape', 5),
    ('honeydew', 7),
    ('kiwi', 1),
    ('lemon', 10),
]


class Person:
    name = "John Smith"
    age = 30
    gender = "male"
    address = "123 Main St"
    phone_number = "555-555-5555"
    email = "johnsmith@example.com"
    is_employed = True


class SuperHero:
    pass


batman = SuperHero()
batman.can_fly = False
batman.damage = 175

superman = SuperHero()
superman.can_fly = True
superman.damage = 285
superman.alter_ego = 'Кларк Кент'


class Config:
    pass

def create_instance(n: int) -> Config:
    obj = Config()
    [setattr(obj, f'attribute{i}', f'value{i}') for i in range(1, n + 1)]
    return obj


if __name__ == '__main__':
    config_2 = create_instance(2)
    assert isinstance(config_2, Config)
    assert config_2.__dict__ == {'attribute1': 'value1', 'attribute2': 'value2'}

    config_4 = create_instance(4)
    assert isinstance(config_4, Config)
    assert config_4.__dict__ == {'attribute1': 'value1',
                                 'attribute2': 'value2',
                                 'attribute3': 'value3',
                                 'attribute4': 'value4'}

    config_7 = create_instance(7)
    assert isinstance(config_7, Config)
    assert config_7.__dict__ == {'attribute1': 'value1', 'attribute2': 'value2',
                                 'attribute3': 'value3', 'attribute4': 'value4',
                                 'attribute5': 'value5',
                                 'attribute6': 'value6',
                                 'attribute7': 'value7'}

    config_10 = create_instance(10)
    assert isinstance(config_10, Config)
    assert config_10.__dict__ == {'attribute1': 'value1', 'attribute2': 'value2',
                                  'attribute3': 'value3', 'attribute4': 'value4',
                                  'attribute5': 'value5', 'attribute6': 'value6',
                                  'attribute7': 'value7', 'attribute8': 'value8',
                                  'attribute9': 'value9', 'attribute10': 'value10'}

    print('good')
