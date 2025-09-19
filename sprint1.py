''' 
Sprint 1 - Core System & User Authentication:
- Implement User, Student, Teacher classes.
- Implement Library with books, users, and passwords dictionaries.
- Add user login/authentication system.
'''
# sprint1.py
class User: # ALL students and teachers share this class (base class)
    def __init__(self, user_id, name, password):
        self.user_id = user_id
        self.name = name
        self.password = password
        self.borrowed_books = []  # used in Sprint 2+

class Student(User): # Inherits from user (sub class)
    def __init__(self, user_id, name, password, major):
        super().__init__(user_id, name, password)
        self.major = major

class Teacher(User):# Inherits from user (sub class)
    def __init__(self, user_id, name, password, subject):
        super().__init__(user_id, name, password)
        self.subject = subject

class Library: # Like system database
    def __init__(self):
        self.users = {}      # user_id -> User
        self.passwords = {}  # user_id -> password

    def register_user(self, user):
        self.users[user.user_id] = user
        self.passwords[user.user_id] = user.password

    def authenticate(self, user_id, password):
        if self.passwords.get(user_id) == password:
            print(f"Login successful for {user_id}")
            return self.users[user_id]
        print("Login failed")
        return None

if __name__ == "__main__":
    lib = Library()
    s1 = Student("s1", "Lizzie", "pw1", "ENCE 420")
    t1 = Teacher("t1", "Dr. Vudumu", "pw2", "ENCE")
    lib.register_user(s1); lib.register_user(t1)

    lib.authenticate("s1", "pw1")   # success
    lib.authenticate("t1", "wrong") # fail

