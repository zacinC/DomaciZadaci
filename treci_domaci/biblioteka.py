class Book:
    def __init__(self, title, author, year, copies):
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def get_copies(self):
        return self.copies

    def set_copies(self, copies):
        self.copies = copies


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book.get_title() == title:
                self.books.remove(book)

    def search_by_title(self, title):
        result = []
        for book in self.books:
            if title.lower() in book.get_title().lower():
                result.append(book)
        return result

    def search_by_author(self, author):
        result = []
        for book in self.books:
            if author.lower() in book.get_author().lower():
                result.append(book)
        return result

    def display_available_books(self):
        print("Available Books:")
        for book in self.books:
            print("Title: ", book.get_title())
            print("Author: ", book.get_author())
            print("Year: ", book.get_year())
            print("Copies: ", book.get_copies())
            print()


def main():
    library = Library()

    while True:
        print("Library Management System")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search by title")
        print("4. Search by author")
        print("5. Display available books")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            year = input("Enter year: ")
            copies = input("Enter number of copies: ")
            book = Book(title, author, year, copies)
            library.add_book(book)
            print("Book added successfully!")

        elif choice == "2":
            title = input("Enter title of the book to remove: ")
            library.remove_book(title)
            print("Book removed successfully!")

        elif choice == "3":
            title = input("Enter title to search: ")
            result = library.search_by_title(title)
            if result:
                print("Matching books:")
                for book in result:
                    print("Title:", book.get_title())
                    print("Author:", book.get_author())
                    print("Year:", book.get_year())
                    print("Copies:", book.get_copies())
                    print()
            else:
                print("No matching books found.")

        elif choice == "4":
            author = input("Enter author to search: ")
            result = library.search_by_author(author)
            if result:
                print("Matching books:")
                for book in result:
                    print("Title:", book.get_title())
                    print("Author:", book.get_author())
                    print("Year:", book.get_year())
                    print("Copies:", book.get_copies())
                    print()
            else:
                print("No matching books found.")

        elif choice == "5":
            library.display_available_books()

        elif choice == "6":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

