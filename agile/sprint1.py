if __name__ == "__main__":
    print("Sprint 1 – starting point (Add/Remove student, Enroll in course).")

students = []

def add_student(student_name):
    students.append(student_name)
    print(f"✅ Student {student_name} ")

def remove_student(student_name):
    if student_name in students:
        students.remove(student_name)
        print(f"❌ Student {student_name} ")
    else:
        print(f"⚠️ {student_name} is not in this class")

# Run the code only if this file is run directly (not when imported)
if __name__ == "__main__":
    add_student("Lizzie")
    remove_student("Lizzie")