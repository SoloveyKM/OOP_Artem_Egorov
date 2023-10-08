class InfinityIterator:

    def __init__(self):
        self.value = 0

    def __iter__(self):
        return self

    def __next__(self):
        value = self.value
        self.value += 10
        return value

if __name__ == '__main__':

    a = iter(InfinityIterator())
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
