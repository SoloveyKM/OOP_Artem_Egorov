class SequenceIterator:

    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return iter(self.data[::2] + self.data[1::2])

