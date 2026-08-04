'''A library stores information about books and digital books. Create a base class Book
with a constructor to initialize book details. Create a derived class EBook that adds file
size information.'''


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size

    def display(self):
        print("Book Title:", self.title)
        print("Author:", self.author)
        print("Pages :",self.pages)
        print("File Size:", self.file_size, "MB")
ebook = EBook("Merchant of Venice", "William Sheaksphere", 267, 20)
ebook.display()