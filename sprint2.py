'''
Sprint 2 – Book Management & Borrow/Return Functionality:
- Implement Book class with total_copies and available_copies.
- Implement borrow/return functionality for users.
- Implement search function for books.

'''

# sprint2.py
from typing import List

# ---------- Book ----------
class Book: # Holds counts and title/author of book
    def __init__(self, book_id, title, author, total_copies, available_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = available_copies

    def borrow_one(self) -> bool:
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        return False

    def return_one(self) -> None:
        if self.available_copies < self.total_copies:
            self.available_copies += 1

# ---------- Users ----------
class User:
    def __init__(self, user_id, name, password):
        self.user_id = user_id
        self.name = name
        self.password = password
        self.borrowed_books: List[str] = []  # list of book_ids

    def borrow_book(self, library: "Library", book_id: str) -> bool:
        book = library.books.get(book_id)
        if not book:
            print(f"[{self.name}] Book {book_id} not found.")
            return False
        if book.borrow_one():
            self.borrowed_books.append(book_id)
            print(f"[{self.name}] Borrowed '{book.title}'.")
            return True
        print(f"[{self.name}] '{book.title}' not available.")
        return False

    def return_book(self, library: "Library", book_id: str) -> bool:
        if book_id not in self.borrowed_books:
            print(f"[{self.name}] You don’t have this book.")
            return False
        book = library.books.get(book_id)
        if not book:
            print(f"[{self.name}] Book record missing.")
            return False
        book.return_one()
        self.borrowed_books.remove(book_id)
        print(f"[{self.name}] Returned '{book.title}'.")
        return True

class Student(User):
    def __init__(self, user_id, name, password, major):
        super().__init__(user_id, name, password)
        self.major = major

class Teacher(User):
    def __init__(self, user_id, name, password, subject):
        super().__init__(user_id, name, password)
        self.subject = subject

# ---------- Library ----------
class Library:
    def __init__(self):
        self.users = {}       # user_id -> User
        self.passwords = {}   # user_id -> password
        self.books = {}       # book_id -> Book

    # users / auth
    def register_user(self, user: User) -> None:
        self.users[user.user_id] = user
        self.passwords[user.user_id] = user.password

    def authenticate(self, user_id: str, password: str):
        if self.passwords.get(user_id) == password:
            print(f"Login successful for {user_id}")
            return self.users[user_id]
        print("Login failed")
        return None

    # books
    def add_book(self, book: Book) -> None:
        self.books[book.book_id] = book

    def remove_book(self, book_id: str) -> bool:
        return self.books.pop(book_id, None) is not None

    def search_book(self, title_substring: str):
        key = title_substring.lower()
        return [b for b in self.books.values() if key in b.title.lower()]

# ---------- Demo (for screenshots) ----------
if __name__ == "__main__":
    lib = Library()

    # register one student to exercise borrow/return
    s1 = Student("s1", "Reese", "pw1", "Software Eng.")
    lib.register_user(s1)

    # add books
    lib.add_book(Book("B1", "Title 1", "Brad Smith", 3, 3))
    lib.add_book(Book("B2", "Title 2", "Rachel Peters", 1, 1))
    lib.add_book(Book("B3", "Title 3", "Geoff Bigly", 2, 2))

    # search
    print("Search 'Title 1':")
    for b in lib.search_book("Title 1"):
        print(f" - {b.title} (avail {b.available_copies}/{b.total_copies})")

    # auth + borrow/return
    user = lib.authenticate("s1", "pw1")  # expect success
    if user:
        s1.borrow_book(lib, "B2")   # OK: goes from 1→0
        s1.borrow_book(lib, "B2")   # Not available now
        s1.return_book(lib, "B2")   # Return: 0→1
        s1.borrow_book(lib, "B9")   # Book not found example
