class FibonacciIterator:

    def __init__(self, n):
        self.n = n
        self.index = 1
        self.num1 = 0
        self.num2 = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > self.n:
            raise StopIteration
        self.index += 1
        result = self.num1
        self.num1, self.num2 = self.num2, self.num1 + self.num2
        return result


if __name__ == '__main__':
    fibonacci_iter = FibonacciIterator(0)

    for number in fibonacci_iter:
        print(number)
