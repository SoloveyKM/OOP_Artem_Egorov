class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_exists(self):
        return self.a < self.b + self.c and self.b < self.a + self.c and self.c < self.b + self.a

    def is_equilateral(self):
        return self.a == self.b == self.c

    def is_isosceles(self):
        if self.is_exists():
            return self.a == self.b or self.c == self.b or self.c == self.a
        return False
