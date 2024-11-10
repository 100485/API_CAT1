class Book:
    def __init__(self, isbn: int, title: str, author: str):
        """
        Added [isbn] to make it easy to pick books
        """
        self.isbn = isbn
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return print(f"- {self.isbn} (ISBN) {self.title} by {self.author} ({self.status()})")
    
    def status(self):
        return "Borrowed" if self.is_borrowed else "Available"

    def mark_as_borrowed(self):
        if self.is_borrowed:
            print(f"The book '{self.title}' is already borrowed.")
        else:
            self.is_borrowed = True
            print(f"The book '{self.title}' has been marked as borrowed.")

    def mark_as_returned(self):
        if not self.is_borrowed:
            print(f"The book '{self.title}' was not borrowed.")
        else:
            self.is_borrowed = False
            print(f"The book '{self.title}' has been marked as returned.")



class LibraryMember:
    def __init__(self, name: str, member_id: int):
        self.name: str = name
        self.member_id: int = member_id
        self.borrowed_books: list[Book] = []

    def borrow_book(self, book, books):
        """
        [book] is the book you want to borrow.
        [books] is the list of books to borrow from.
        """
        if book.is_borrowed:
            print(f"Sorry, the book '{book.title}' is currently unavailable.")
            # Suggest other available books
            available_books = [b for b in books if not b.is_borrowed]
            if available_books:
                print("Here are other books currently available:")
                for b in available_books:
                    print(b)
            else:
                print("No other books are available at the moment.")
        else:
            book.mark_as_borrowed()
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed the book '{book.title}'.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned the book '{book.title}'.")
        else:
            print(f"{self.name} does not have the book '{book.title}' to return.")

    def list_borrowed_books(self):
        if not self.borrowed_books:
            print(f"{self.name} has no borrowed books.")
        else:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(book)


def _find_book(isbn: str, books: list[Book]):
    """
    Helper function to find the book inside [books] with the given [isbn]
    """
    for book in books:
        if book.isbn == isbn:
            return book
    return None

# Interactive code
def main():
    # Sample books
    books = [
        Book(1, "Learn 123", "Antisha Math"),
        Book(2, "Learn abc", "Patri Kim"),
        Book(3, "Learn Language", "Lidi Lugha"),
        Book(4, "Learn Sci", "Bio Logy"),
        Book(5, "Learn Chem", "Periodic Tee"),
        Book(6, "Learn Phy", "Izo Newt"),
    ]

    # Sample member
    member = LibraryMember("Keletu", "L0001")

    while True:
        print("\nLibrary System")
        print("1. List all books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. List borrowed books")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nAvailable Books:")
            for book in books:
                print(book)

        elif choice == "2":
            typed_isbn = input("\nEnter the ISBN of the book to borrow: ")
            typed_isbn_to_int = int(typed_isbn.strip())
            book_to_borrow = _find_book(typed_isbn_to_int, books)
            if book_to_borrow:
                member.borrow_book(book_to_borrow, books)
            else:
                print("Book not found.")

        elif choice == "3":
            typed_isbn = input("\nEnter the ISBN of the book to return: ")
            typed_isbn_to_int = int(typed_isbn.strip())
            book_to_return = _find_book(typed_isbn_to_int, books)
            if book_to_return:
                member.return_book(book_to_return)
            else:
                print("Book not found.")

        elif choice == "4":
            member.list_borrowed_books()

        elif choice == "5":
            print("Exiting the library system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
