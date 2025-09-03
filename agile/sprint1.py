students = []
courses = {}

def add_student(student_name):
    students.append(student_name)
    print(f"✅ {student_name} has been added.\n")

def remove_student(student_name):
    if student_name in students:
        students.remove(student_name)
        print(f"❌ {student_name} has been removed.\n")
    else:
        print(f"⚠️ {student_name} is not in the student list.\n")

def add_to_course(student_name, course_name):
    if student_name in students:
        if course_name not in courses:
           courses[course_name] = []

    
        if student_name not in courses[course_name]:
            courses[course_name].append(student_name)
            print(f"{student_name} has been added to {course_name}")
        else:
            print(f"{student_name} is already enrolled in {course_name}")
    else:
        print(f"⚠️ {student_name} is not in the student list.")

# Run the code only if this file is run directly (not when imported)
if __name__ == "__main__":
    print("Sprint 1 – starting point (Add/Remove student, Enroll in course).")
    add_student("Lizzie")
    remove_student("Lizzie")
    add_student("Lizzie")
    add_to_course("Lizzie", "Math")
    add_to_course("Lizzie", "Math")  # test duplicate
    remove_student("Luanne") # test non-existent student
    add_to_course("Luanne", "Science")
    print(courses)