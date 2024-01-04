try:
    a = int(input())
    b = int(input())
    print(f"Результат деления a на b: {a/b}")
except ValueError:
    print("Введите целое число")
except ZeroDivisionError:
    print("Делитель не должен быть равен нулю")
