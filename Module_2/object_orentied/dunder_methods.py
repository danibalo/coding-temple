class Book:
    """Represents a physical book."""

    def __init__(self, title, author, year, pages):
        # Validate that year is a positive integer
        if not isinstance(year, int) or year <= 0:
            raise ValueError("Year must be a positive integer")

        # Initialize book attributes
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

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
    def __eq__(self, other):
        return (
            self.title == other.title and 
            self.author == other.author
        )
    def __lt__(self, other):
        return self.pages < other.pages
    def __len__(self):
        return self.pages
    def __contains__(self, keyword):
        return keyword.lower() in self.title.lower()

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
book1 = Book("Python for Advanced system", "Pr James White", 2004, 567)
book2 = Book("Python for Beginners", "Mark keiv", 2000, 500)
print(book1 == book2)
print(len(book2))
print(book2 < book1)
print("Py" in book1)

