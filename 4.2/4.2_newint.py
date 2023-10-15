class NewInt(int):

    def repeat(self, n=2):
        return int(str(self) * n)

    def to_bin(self):
        return int(bin(self)[2:])


if __name__ == '__main__':

    a = NewInt(9)
    print(a.repeat())  # печатает число 99
    d = NewInt(a + 5)
    print(d.repeat(3))  # печатает число 141414
    b = NewInt(NewInt(7) * NewInt(5))
    print(b.to_bin())  # печатает 10001