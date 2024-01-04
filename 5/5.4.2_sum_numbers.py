def sum_numbers(numbers):
    if not isinstance(numbers, list):
        raise TypeError('Аргумент numbers должен быть списком')
    if len(numbers) == 0:
        raise ValueError("Пустой список")
    for i in numbers:
        if not isinstance(i, (int, float)):
            raise TypeError('Неправильный тип элемента')
    return  sum(numbers)


if __name__ == '__main__':
    for value in (True, (1, 2, 3), {1: 'hello'}, {1, 2, 3}):
        try:
            result = sum_numbers(value)
        except TypeError as error:
            print(error)

    try:
        result = sum_numbers([])
    except ValueError as error:
        print(error)

    try:
        sum_numbers([1, 'hello', 2, 3])
    except TypeError as error:
        print(error)

    try:
        sum_numbers([1, 2, 3, 4, 5, [1, 2, 3]])
    except TypeError as error:
        print(error)

    try:
        sum_numbers([1, 2, 3, 4, 5, {1, 2, 3}])
    except TypeError as error:
        print(error)

    try:
        sum_numbers([1, 2, 3, 4, 5, (1, 2, 3)])
    except TypeError as error:
        print(error)

    assert sum_numbers([1, 2, 3, 4, 5]) == 15
    assert sum_numbers([1, 2, 3, 4, 5.0]) == 15.0