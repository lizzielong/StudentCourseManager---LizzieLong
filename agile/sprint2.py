from typing import Dict, List, Set

# define blueprint for making student objects (like a template)
class Student:
    #__init__ runs whenever student object is created
    def __init__(self, name: str):
        self.name = name
        self.grades: Dict[str, List[float]] = {}
        # creates empty dictionary where key = course name and value = list of grades for the course

    def enroll(self, course: str):
        # If course is not already in the dictionary, it adds it with an empty list of grades
        if course not in self.grades:
            self.grades[course] = []

    def unenroll(self, course: str):
        # removes course entry for student object (deletes key/value pair from dictionary)
        if course in self.grades:
            del self.grades[course]

    def add_grade(self, course: str, grade: float):
        # adds number into list of grades for course
        if course not in self.grades:
            raise ValueError(f"{self.name} is not in {course}.")
        self.grades[course].append(grade)

    def __str__(self):
        # __str__ : when someone prints a student object, show their name and courses
        if not self.grades:
            return f"{self.name} is not in any courses"
        parts = []
        for g, grades in sorted(self.grades.items()):
            if grades:
                parts.append(f"{g}: {grades}")
            else:
                parts.append(f"{g}:[]")
        # combines pieces into one string with "," in between
        return f"{self.name}: " + ",".join(parts)

# Now I want to create something to organize the entire system, calling it "gradebook"
class GradeBook:
    def __init__(self):
        self.students: Dict[str, Student] = {}
        self.course_catalog: Set[str] = set()
        # catalog for a set of course names

    # update add student from Sprint 1
    def add_student(self, name: str):
        if name in self.students:
            print(f"{name} already exists.\n")
            return
        self.students[name] = Student(name)
        print(f"{name} has been added.\n")

    def remove_student(self, name: str):
        if name in self.students:
            del self.students[name]
            print(f"{name} has been removed.")
        else:
            print(f"{name} is not found.")

    def enroll_in_course(self, name: str, course: str):
        if name not in self.students:
            print(f"{name} is not found.")
            return
        if course not in self.course_catalog:
            print(f"{course} does not exist. ")
            return
        self.students[name].enroll(course)
        print(f"{name} has been added to {course}.")

    def add_course(self, course: str):
        if course in self.course_catalog:
            print(f"{course} already exists.")
            return
        self.course_catalog.add(course)
        print(f"{course} added to catalog.")

    def remove_course(self, course: str):
        if course not in self.course_catalog:
            print(f"{course} not found in catalog.")
            return
        # Remove from catalog
        self.course_catalog.remove(course)
        # Unenroll all students from this course
        for s in self.students.values():
            s.unenroll(course)
        print(f"{course} removed from catalog and all students unenrolled.")

    def assign_grade(self, name: str, course: str, grade: float):
        if name not in self.students:
            print(f"{name} not found.")
            return
        if course not in self.course_catalog:
            print(f"{course} does not exist in catalog.")
            return
        try:
            self.students[name].add_grade(course, float(grade))
            print(f"{grade} added to '{name}' for '{course}'.")
        except ValueError as e:
            print(f"⚠️  {e}")

    def list_courses(self):
        if not self.course_catalog:
            print("No courses in catalog.")
            return
        print("Courses in catalog:")
        for c in sorted(self.course_catalog):
            print("  •", c)
    def list_students(self):
        if not self.students:
            print("No students yet.")
            return
        print("\nStudents:")
        for s in sorted(self.students.values(), key=lambda x: x.name.lower()):
            print("  •", s)
        print()

def menu():
    gm = GradeBook()

    while True:
        print("\n=== Sprint 2 Menu ===")
        print("1) Add course")
        print("2) Remove course")
        print("3) Add student (from Sprint 1)")
        print("4) Enroll student in a course (from Sprint 1)")
        print("5) Assign grade to student in a course")
        print("6) List courses")
        print("7) List students and their grades")
        print("8) Exit")
        choice = input("Choose an option (1-8): ").strip()

        if choice == "1":
            course = input("Course name: ").strip()
            if course:
                gm.add_course(course)
            else:
                print("Please enter a non-empty course name.")

        elif choice == "2":
            course = input("Course to remove: ").strip()
            if course:
                gm.remove_course(course)
            else:
                print("Please enter a non-empty course name.")

        elif choice == "3":
            name = input("Student name: ").strip()
            if name:
                gm.add_student(name)
            else:
                print("Please enter a non-empty name.")

        elif choice == "4":
            name = input("Student name: ").strip()
            course = input("Course name: ").strip()
            if name and course:
                gm.enroll_in_course(name, course)
            else:
                print("Please enter both a student name and a course name.")

        elif choice == "5":
            name = input("Student name: ").strip()
            course = input("Course name: ").strip()
            grade_str = input("Grade (number): ").strip()
            if not (name and course and grade_str):
                print("Please enter a student, course, and grade.")
            else:
                try:
                    gm.assign_grade(name, course, float(grade_str))
                except ValueError:
                    print("Grade must be a number (e.g., 95 or 87.5).")

        elif choice == "6":
            gm.list_courses()

        elif choice == "7":
            gm.list_students()

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Please choose a valid option (1-8).")
        



if __name__ == "__main__":
    print("Sprint 2 – Add/Remove courses, assign grades.")
    print("Upgrading code from Sprint 1 and adding new capabilities")
    menu()
