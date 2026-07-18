class Book:
    """Represents a physical book."""

    def __init__(self, title, author, year):
        # Validate that year is a positive integer
        if not isinstance(year, int) or year <= 0:
            raise ValueError("Year must be a positive integer")

        # Initialize book attributes
        self.title = title
        self.author = author
        self.year = year

        # Book starts as available
        self.checked_out = False

    def check_out(self):
        """Check out the book if it is available."""

        # If already checked out, checkout fails
        if self.checked_out:
            return False

        # Mark the book as checked out
        self.checked_out = True
        return True

    def return_book(self):
        """Return the book."""

        # Can't return a book that wasn't checked out
        if not self.checked_out:
            return False

        # Make the book available again
        self.checked_out = False
        return True

    def __repr__(self):
        # Display the current status
        status = "Checked out" if self.checked_out else "Available"

        # String representation of the object
        return (
            f"Book(title='{self.title}', "
            f"author='{self.author}', "
            f"year={self.year}, "
            f"status='{status}')"
        )


class EBook(Book):
    """Represents an electronic book."""

    def __init__(self, title, author, year, file_size_mb):
        # Initialize inherited attributes
        super().__init__(title, author, year)

        # Store additional ebook information
        self.file_size_mb = file_size_mb

        # Number of users currently using this ebook
        self.check_out_count = 0

    def check_out(self):
        """
        Unlike physical books, ebooks can be checked out
        by multiple users at the same time.
        """

        # Increase number of active users
        self.check_out_count += 1
        return True

    def return_book(self):
        """One user returns the ebook."""

        # No one has the ebook
        if self.check_out_count == 0:
            return False

        # Reduce active user count
        self.check_out_count -= 1
        return True

    def __repr__(self):
        # Determine ebook status
        status = (
            "Available"
            if self.check_out_count == 0
            else f"Checked out by {self.check_out_count} users"
        )

        # Return formatted ebook information
        return (
            f"EBook(title='{self.title}', "
            f"author='{self.author}', "
            f"year={self.year}, "
            f"file_size={self.file_size_mb} MB, "
            f"status='{status}')"
        )


class Catalog:
    """Manages a collection of books."""

    def __init__(self):
        # Store all books in a list
        self.books = []

    def add_book(self, book):
        """Add a Book or EBook to the catalog."""

        # Only Book objects (or subclasses) are allowed
        if not isinstance(book, Book):
            raise TypeError("Only Book or EBook objects can be added.")

        self.books.append(book)

    def search_by_author(self, author):
        """
        Return all books written by the given author.
        Search is case-insensitive.
        """
        return [
            book
            for book in self.books
            if book.author.lower() == author.lower()
        ]

    def search_by_title(self, keyword):
        """
        Return books whose title contains the keyword.
        Search is case-insensitive.
        """
        return [
            book
            for book in self.books
            if keyword.lower() in book.title.lower()
        ]

    def get_available(self):
        """
        Return all available books.
        Physical books must not be checked out.
        EBooks are always available because
        multiple users can borrow them.
        """

        available_books = []

        for book in self.books:

            # Every ebook is considered available
            if isinstance(book, EBook):
                available_books.append(book)

            # Physical books are available only if not checked out
            elif not book.checked_out:
                available_books.append(book)

        return available_books

    def summary(self):
        """Print a summary of the catalog."""

        # Total number of books
        total = len(self.books)

        # Count only physical books
        physical_books = sum(
            1 for book in self.books if type(book) is Book
        )

        # Count ebooks
        ebooks = sum(
            1 for book in self.books if isinstance(book, EBook)
        )

        # Count available books
        available_books = len(self.get_available())

        print("***** Catalog Summary *****")
        print(f"Total books: {total}")
        print(f"Physical books: {physical_books}")
        print(f"EBooks: {ebooks}")
        print(f"Available books: {available_books}")

        # Print every book in the catalog
        for book in self.books:
            print(book)
catalog = Catalog()
catalog.add_book(Book("Python Crash Course", "Eric Matthes", 2019))
catalog.add_book(Book("Clean Code", "Robert Martin", 2008))
catalog.add_book(EBook("AI Engineering", "Chip Huyen", 2025, 15.2))

# Search
results = catalog.search_by_title("python")
print(results)  # Should find "Python Crash Course"

# Check out
catalog.books[0].check_out()
available = catalog.get_available()
print(f"Available: {len(available)} books")

catalog.summary()
