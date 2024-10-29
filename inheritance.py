# managing a library system
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def  display_info(self):
        return f"The title: {self.title}, Author: {self.author}, Year: {self.year}"

# child class

class LibraryBook(Book):  #its inhereting traits from above
    def __init__(self, title, author, year,isbn, copiesavailable):
        super().__init__(title, author, year)
        self.copiesavailable = int(copiesavailable)
        self.isbn = isbn

    def borrow_book(self):
        if self.copiesavailable > 0:
            self.copiesavailable -=1
            return f"{self.title} borrowed. Copies left: {self.copiesavailable}"
        else:
            return f"No of copies {self.title} unavailable"
    def return_book(self):
        self.copiesavailable +=1
        return f"{self.title} borrowed. Copies left: {self.copiesavailable}"

#usage example
book1=LibraryBook("The art of War", "Tsu", "Year1", "ISBN1", "20")
print(book1.display_info())

print(book1.borrow_book())

print(book1.return_book())
