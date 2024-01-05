class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __iter__(self):
        return LibraryIterator(self.books)  # тут определите, что будете передавать итератору


class LibraryIterator:

    def __init__(self, books):
        self.books = books
        self.max = len(books)
        self.book_index = 0
        self.page_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.book_index == self.max:
            raise StopIteration
        result = self.books[self.book_index].pages[self.page_index]
        self.page_index += 1
        if self.page_index == len(self.books[self.book_index].pages):
            self.book_index += 1
            self.page_index = 0
        return result


if __name__ == '__main__':

    # Пример использования
    book1 = Book("Book 1", ["Page 1", "Page 2", "Page 3", "Page 4"])
    book2 = Book("Book 2", ["Page A", "Page B", "Page C"])
    book3 = Book("Book 3", ["Chapter 1", "Chapter 2"])

    library = Library()
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Используем вложенный итератор для обхода страниц в библиотеке
    for page in library:
        print(page)
