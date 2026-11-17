class Student:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        self.courses = {}

    def add_course(self, course, grade):
        self.courses[course] = grade
        return True

    def change_grade(self, course, grade):
        if (course in self.courses):
            self.courses[course] = grade
            return True
        else:
            return False

    def calculate_GPA(self):
        if (len(self.courses) == 0):
            return 0.0
        else:
            return sum(self.courses.values())/len(self.courses)

    def show_grades(self):
        print(f'Student Name: {self.name}')
        print(f'Student ID: {self.id}')
        print(f'Student email: {self.email}')
        print(f'{self.name}\'s courses and grades:')
        for course, grade in self.courses.items():
            print(f'Course: {course}; Grade: {grade}')
        return True

class CourseManagementSystem():
    def __init__(self):
        self.students = []

    '''
    Display a student's average grade.
    '''
    def add_student(self, id, name, email):
        new_student = Student(id, name, email)
        for student in self.students:
            if student.id == id:
                return False
        self.students.append(new_student)
        return True

    def find_student_from_id(self, id):
        for student in self.students:
            if student.id == id:
                return student
        return False

    def remove_student(self, id):
        for student in self.students:
            if student.id == id:
                self.students.remove(student)
                return True
        return False

    def display_students(self):
        for student in self.students:
            print(student.name)
        return True

    def enroll_student(self, id, course, grade):
        for student in self.students:
            if student.id == id:
                student.add_course(course, grade)
                return True
        return False

    def update_grade(self, id, course, grade):
        for student in self.students:
            if student.id == id:
                student.change_grade(course, grade)
                return True
        return False

    def display_GPA(self, id):
        for student in self.students:
            if student.id == id:
                return student.calculate_GPA()
        return False
