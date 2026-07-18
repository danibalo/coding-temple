# Build a Library Catalog
## Objective
- Design and implement a class hierarchy for manging a collection of books.
## 1. Book Class
  * Attributes: title, author, year, checked_out(False)
  * Methods: check_out(), return_book(), __repr__ (shows title, author, and status)
  * Validation: year must be a positive integer
## 2. EBook class (inherits from Book)
  * Additional attribute: file_size_mb
  * Override __repr__ to include file size
  * Override check_out() , ebooks can be checked out by multiple people simultaneously (hint: use a counter instead of a boolean)
## 3.Catalog class
  * Methods: add_book(book), search_by_author(author), search_by_title(keyword), get_available(), summary()
  * search_by_title should find books where the keyword appears anywhere in the title (case-insensitive)

## Test code:

catalog = Catalog() catalog.add_book(Book("Python Crash Course", "Eric Matthes", 2019))
catalog.add_book(Book("Clean Code", "Robert Martin", 2008))
catalog.add_book(EBook("AI Engineering", "Chip Huyen", 2025, 15.2))

### Search
results = catalog.search_by_title("python")
print(results)  # Should find "Python Crash Course"

### Check out
catalog.books[0].check_out()
available = catalog.get_available()
print(f"Available: {len(available)} books")

catalog.summary()
