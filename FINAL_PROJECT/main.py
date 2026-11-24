class Student:
    '''
    Student class with info for each student and helper functions like getters and setters
    '''
    def __init__(self, student_id, name, email):
        self.id = student_id
        self.name = name
        self.email = email
        self.courses = {}

    def add_course(self, course, grade):
        if course in self.courses:
            return False
        self.courses[course] = grade
        return True

    def change_grade(self, course, grade):
        if course in self.courses:
            self.courses[course] = grade
            return True
        return False

    def calculate_average(self):
        if len(self.courses) == 0:
            return 0.0
        return sum(self.courses.values()) / len(self.courses)

    def get_info(self):
        info = (
            f"Student Name: {self.name}\n"
            f"Student ID: {self.id}\n"
            f"Student Email: {self.email}\n"
            f"{self.name}'s Courses and Grades:"
        )
        if not self.courses:
            info += "\n  No courses enrolled yet."
        else:
            for course, grade in self.courses.items():
                info += f"\n  Course: {course}; Grade: {grade}"
        return info


class CourseManagementSystem:
    '''
    Data class with all the student implementation of each student and such
    '''
    def __init__(self):
        self.students = []

    def add_student(self, student_id, name, email):
        if self.find_student_from_id(student_id) is not None:
            return False
        new_student = Student(student_id, name, email)
        self.students.append(new_student)
        return True

    def find_student_from_id(self, student_id):
        for student in self.students:
            if student.id == student_id:
                return student
        return None

    def remove_student(self, student_id):
        student = self.find_student_from_id(student_id)
        if student is not None:
            self.students.remove(student)
            return True
        return False

    def get_all_students(self):
        return self.students

    def enroll_student(self, student_id, course, grade):
        student = self.find_student_from_id(student_id)
        if student is not None:
            return student.add_course(course, grade)
        return False

    def update_grade(self, student_id, course, grade):
        student = self.find_student_from_id(student_id)
        if student is not None:
            return student.change_grade(course, grade)
        return False

    def get_student_average(self, student_id):
        student = self.find_student_from_id(student_id)
        if student is not None:
            return student.calculate_average()
        return None



'''
print menu helper class
'''
def print_menu():
    print("\nStudent Course Management System\n")
    print("1. Add a New Student")
    print("2. Search for a Student")
    print("3. Remove a Student")
    print("4. Display All Students")
    print("5. Enroll a Student in a Course")
    print("6. Update a Student's Grade")
    print("7. Display a Student's Average Grade")
    print("8. Exit\n")
    return input("Enter your choice (1-8): ").strip()

'''
check grade helper class (if its a valid grade)
'''
def get_valid_grade():
    while True:
        raw_grade = input("Enter Grade (0-100): ").strip()
        try:
            grade = float(raw_grade)
            if 0 <= grade <= 100:
                return grade
            print("Invalid grade. Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric grade.")

def main():
    '''
    Main function to print everything
    '''
    system = CourseManagementSystem()


    '''
    Used a while True loop so its easy to break out of (just put the break keyword)
    '''
    while True:
        choice = print_menu()
        print()

        if choice == "1":
            student_id = input("Enter Student ID: ").strip()
            name = input("Enter Student Name: ").strip()
            email = input("Enter Student Email: ").strip()

            if not student_id or not name or not email:
                print("Error: Student ID, name, and email cannot be empty.")
            elif system.add_student(student_id, name, email):
                print("Student added successfully!")
            else:
                print(f"Error: A student with ID '{student_id}' already exists.")

        elif choice == "2":
            student_id = input("Enter Student ID: ").strip()
            student = system.find_student_from_id(student_id)
            if student is not None:
                print(student.get_info())
            else:
                print(f"Student with ID '{student_id}' not found.")

        elif choice == "3":
            student_id = input("Enter Student ID: ").strip()
            if system.remove_student(student_id):
                print("Student removed successfully!")
            else:
                print(f"Student with ID '{student_id}' not found.")

        elif choice == "4":
            students = system.get_all_students()
            if not students:
                print("No students are currently in the system.")
            else:
                print("All Enrolled Students:")
                for student in students:
                    print(f"ID: {student.id} | Name: {student.name} | Email: {student.email}")

        elif choice == "5":
            student_id = input("Enter Student ID: ").strip()
            student = system.find_student_from_id(student_id)
            if student is None:
                print(f"Student with ID '{student_id}' not found.")
            else:
                course = input("Enter Course Code: ").strip().upper()
                grade = get_valid_grade()
                if system.enroll_student(student_id, course, grade):
                    print("Course added successfully!")
                else:
                    print(f"Student is already enrolled in {course}. Use Option 6 to update the grade.")

        elif choice == "6":
            student_id = input("Enter Student ID: ").strip()
            student = system.find_student_from_id(student_id)
            if student is None:
                print(f"Student with ID '{student_id}' not found.")
            else:
                course = input("Enter Course Code: ").strip().upper()
                if course not in student.courses:
                    print(f"Error: {student.name} is not enrolled in {course}.")
                else:
                    grade = get_valid_grade()
                    system.update_grade(student_id, course, grade)
                    print("Grade updated successfully!")

        elif choice == "7":
            student_id = input("Enter Student ID: ").strip()
            student = system.find_student_from_id(student_id)
            if student is not None:
                avg = system.get_student_average(student_id)
                print(f"Student Name: {student.name}")
                print(f"Average Grade: {avg:.1f}")
            else:
                print(f"Student with ID '{student_id}' not found.")

        elif choice == "8":
            print("Thank you for using the Student Course Management System.")
            break
        else:
            print("Not allowed choice. Enter a number between 1 and 8.")


main()
