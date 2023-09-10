class BookShelf:
    def __init__(self, *books): # *books used to pass multi obj/arg
        self.name = books

    def __str__(self):
        return f"Bookshelf with '{len(self.name)}' books in it."

class Book:
    def __init__(self, name):
        self.name  = name

    def __str__(self):
        return f"Book '{self.name}'"

book = Book("Harry Potter")
book2 = Book("The Faith")

shelf = BookShelf(book, book2)
print(book)
print(shelf)
