class FileReader:
    def __init__(self, filename):
        self.file = open(filename)

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline().strip()
        if not line:
            raise StopIteration
        return line

for line in FileReader('lorem.txt'):
    print(line)
