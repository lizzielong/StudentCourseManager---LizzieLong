'''
Sprint 3 – Unique Functions for Students & Teachers:
- Add view_grades() and request_recommendation() for Student.
- Add add_course_material() and review_borrowed_books() for Teacher.
'''

# sprint3.py
from typing import List

# ---------- Domain ----------
class Book:
    def __init__(self, book_id: str, title: str, author: str, total_copies: int, available_copies: int):
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
    def __init__(self, user_id: str, name: str, password: str):
        self.user_id = user_id
        self.name = name
        self.password = password
        self.borrowed_books: List[str] = []

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
    def __init__(self, user_id: str, name: str, password: str, major: str):
        super().__init__(user_id, name, password)
        self.major = major

    # --- Unique methods (Sprint 3) ---
    def view_grades(self) -> None:
        """Simulate viewing grades (simple stub for assignment)."""
        print(f"[Student:{self.name}] Viewing grades… (stub)")

    def request_recommendation(self) -> None:
        """Simulate asking for a book recommendation."""
        print(f"[Student:{self.name}] Recommended: Intro to {self.major} (stub)")


class Teacher(User):
    def __init__(self, user_id: str, name: str, password: str, subject: str):
        super().__init__(user_id, name, password)
        self.subject = subject

    # --- Unique methods (Sprint 3) ---
    def add_course_material(self) -> None:
        """Simulate adding teaching materials."""
        print(f"[Teacher:{self.name}] Added materials for {self.subject} (stub)")

    def review_borrowed_books(self, library: "Library") -> None:
        """
        Show a simple report of what students have borrowed.
        (Here we print book IDs; you could look up titles, too.)
        """
        print(f"[Teacher:{self.name}] Students’ borrowed books:")
        for u in library.users.values():
            if isinstance(u, Student):
                print(f"  - {u.name}: {u.borrowed_books}")


# ---------- Library ----------
class Library:
    def __init__(self):
        self.users = {}       # user_id -> User
        self.passwords = {}   # user_id -> password
        self.books = {}       # book_id -> Book

    # Users/auth
    def register_user(self, user: User) -> None:
        self.users[user.user_id] = user
        self.passwords[user.user_id] = user.password

    def authenticate(self, user_id: str, password: str) -> User | None:
        if self.passwords.get(user_id) == password:
            print(f"Login successful for {user_id}")
            return self.users[user_id]
        print("Login failed")
        return None

    # Books
    def add_book(self, book: Book) -> None:
        self.books[book.book_id] = book

    def search_book(self, title_substring: str) -> List[Book]:
        key = title_substring.lower()
        return [b for b in self.books.values() if key in b.title.lower()]


# ---------- Demo for screenshots ----------
if __name__ == "__main__":
    lib = Library()

    # Users
    lizzie = Student("S1", "Lizzie", "pw1", "Software Engineering")
    reese   = Student("S2", "Reese",   "pw2", "Computer")
    ada  = Teacher("T1", "Dr. Ada",  "pw3", "SE")

    for u in (reese, ada, lizzie):
        lib.register_user(u)

    # Books (titles can be anything you used in Sprint 2)
    lib.add_book(Book("B1", "Title 1", "Author A", 2, 2))
    lib.add_book(Book("B2", "Title 2", "Author B", 1, 1))

    # Auth + basic borrow to populate data
    lib.authenticate("S1", "pw1")
    lizzie.borrow_book(lib, "B1")
    reese.borrow_book(lib, "B2")

    # Unique methods
    print()
    lizzie.view_grades()
    reese.request_recommendation()
    ada.add_course_material()

    # Teacher’s review (simple report)
    print()
    ada.review_borrowed_books(lib)
