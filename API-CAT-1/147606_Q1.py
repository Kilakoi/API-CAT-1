
class Book:
    def Details(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        self.is_borrowed = True

    def mark_as_returned(self):
        self.is_borrowed = False


class LibraryMember:
    def Details(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.mark_as_borrowed()
            self.borrowed_books.append(book)
            print(f"Borrowed: {book.title}")
        else:
            print(f"The book '{book.title}' is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
            print(f"Returned: {book.title}")
        else:
            print(f"The book '{book.title}' was not borrowed by you.")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name}'s Borrowed Books:")
            for book in self.borrowed_books:
                print(f"- {book.title}")
        else:
            print(f"{self.name} has no borrowed books.")


def main():
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    member = LibraryMember("John Doe", "M001")

    member.borrow_book(book1)
    member.list_borrowed_books()
    member.return_book(book1)
    member.list_borrowed_books()

if __name__ == "__main__":
    main()
