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
        