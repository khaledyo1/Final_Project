class Course:
    course_id_counter = 1

    def __init__(self, course_name, course_level):
        self.course_id = Course.course_id_counter
        Course.course_id_counter += 1
        self.course_name = course_name
        self.course_level = course_level

class Student:
    student_id_counter = 1

    def __init__(self, student_name, student_level):
        self.student_id = Student.student_id_counter
        Student.student_id_counter += 1
        self.student_name = student_name
        self.student_level = student_level
        self.student_courses = []

    def add_course(self, course):
        if self.student_level == course.course_level:
            self.student_courses.append(course)
            print(f"Course '{course.course_name}' added to {self.student_name}'s courses.")
        else:
            print("Course level does not match the student's level. Course not added.")

    def display_student_details(self):
        print(f"Name: {self.student_name}")
        print(f"Class: {self.student_level}")
        print("Courses Enrolled:")
        for course in self.student_courses:
            print(f"- {course.course_name}")

def main():
    students = []

    while True:
        print("\nSelect choice please:")
        print("1. Add new student.")
        print("2. Remove student.")
        print("3. Edit student.")
        print("4. Display all students.")
        print("5. Create new student.")
        print("6. Add course to student.")
        print("7. Exit.")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_name = input("Enter student name: ")
            student_level = input("Enter student level (A/B/C): ").upper()
            while student_level not in ["A", "B", "C"]:
                student_level = input("Invalid level. Enter student level (A/B/C): ").upper()
            students.append(Student(student_name, student_level))
            print("Student saved successfully.")

        elif choice == "2":
            student_id = int(input("Enter student ID: "))
            for student in students:
                if student.student_id == student_id:
                    students.remove(student)
                    print("Delete done successfully.")
                    break
            else:
                print("User does not exist.")

        elif choice == "3":
            student_id = int(input("Enter student ID: "))
            for student in students:
                if student.student_id == student_id:
                    new_name = input("Enter new name: ")
                    new_level = input("Enter new level (A/B/C): ").upper()
                    while new_level not in ["A", "B", "C"]:
                        new_level = input("Invalid level. Enter new level (A/B/C): ").upper()
                    student.student_name = new_name
                    student.student_level = new_level
                    print("Edit done successfully.")
                    break
            else:
                print("User does not exist.")

        elif choice == "4":
            print("\nAll Students:")
            for student in students:
                student.display_student_details()

        elif choice == "5":
            student_name = input("Enter student name: ")
            student_level = input("Enter student level (A/B/C): ").upper()
            while student_level not in ["A", "B", "C"]:
                student_level = input("Invalid level. Enter student level (A/B/C): ").upper()
            students.append(Student(student_name, student_level))
            print("Student created successfully.")

        elif choice == "6":
            student_id = int(input("Enter student ID: "))
            for student in students:
                if student.student_id == student_id:
                    course_id = int(input("Enter course ID: "))
                    for course in courses:
                        if course.course_id == course_id:
                            student.add_course(course)
                            break
                    else:
                        print("Course does not exist.")
                    break
            else:
                print("User does not exist.")

        elif choice == "7":
            break

        input("Press Enter to return to the main menu.")

if __name__ == "__main__":
    courses = [Course("Math", "A"), Course("English", "B"), Course("Science", "C")]
    main()
