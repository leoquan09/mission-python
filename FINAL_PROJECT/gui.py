import tkinter as tk
from tkinter import messagebox

'''
Course management program (but with a gui)

All the classes are pretty much the same besides the for the addition of the newest
class: student management gui!! All it does is create all the buttons and callback
functions so that you can just create a new instance of the gui class in the if main
thing while passing the window instance that you create so that the class can access
the window instance that you created in the main outside scope rather than the local
scope of the class (idek if a class can make a window in its scope though). The class
has some more documentation on it but it's pretty self explanatory. It makes buttons,
entries, message boxes (alerts), labels, and frames and then adds a bunch of callbacks
to the buttons. Each component is stored in a frame to make it easier to display by
just packing each frame sequentially and everything just loads top down perfectly :)
'''

class Student:
    '''
    Class to make a single student with helper functions attached to it like getters and setters
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
    Course management class. It has all the implentations for the student class
    '''
    def __init__(self):
        self.students = []

    def add_student(self, student_id, name, email):
        if self.find_student_from_id(student_id):
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
        if student:
            self.students.remove(student)
            return True
        return False

    def get_all_students(self):
        return self.students

    def enroll_student(self, student_id, course, grade):
        student = self.find_student_from_id(student_id)
        if student:
            return student.add_course(course, grade)
        return False

    def update_grade(self, student_id, course, grade):
        student = self.find_student_from_id(student_id)
        if student:
            return student.change_grade(course, grade)
        return False

    def get_student_average(self, student_id):
        student = self.find_student_from_id(student_id)
        if student:
            return student.calculate_average()
        return None


class StudentManagementGUI:
    '''
    Main ui code below in this class
    '''
    def __init__(self, window):
        '''
            The constructor... basically just all the ui because the the callbacks are below this
        '''
        self.window = window
        self.window.title("Student Course Management System")
        self.window.geometry("600x520")
        
        self.system = CourseManagementSystem()

        input_frame = tk.LabelFrame(window, text="Student & Course Details", padx=10, pady=10)
        input_frame.pack(fill="x", padx=15, pady=10)

        tk.Label(input_frame, text="Student ID:").grid(row=0, column=0, sticky="w", pady=3)
        self.id_entry = tk.Entry(input_frame, width=35)
        self.id_entry.grid(row=0, column=1, pady=3, padx=5)

        tk.Label(input_frame, text="Student Name:").grid(row=1, column=0, sticky="w", pady=3)
        self.name_entry = tk.Entry(input_frame, width=35)
        self.name_entry.grid(row=1, column=1, pady=3, padx=5)

        tk.Label(input_frame, text="Student Email:").grid(row=2, column=0, sticky="w", pady=3)
        self.email_entry = tk.Entry(input_frame, width=35)
        self.email_entry.grid(row=2, column=1, pady=3, padx=5)

        tk.Label(input_frame, text="Course Code:").grid(row=3, column=0, sticky="w", pady=3)
        self.course_entry = tk.Entry(input_frame, width=35)
        self.course_entry.grid(row=3, column=1, pady=3, padx=5)

        tk.Label(input_frame, text="Grade (0-100):").grid(row=4, column=0, sticky="w", pady=3)
        self.grade_entry = tk.Entry(input_frame, width=35)
        self.grade_entry.grid(row=4, column=1, pady=3, padx=5)

        btn_frame = tk.Frame(window)
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="1. Add Student", width=22, command=self.add_student).grid(row=0, column=0, padx=5, pady=3)
        tk.Button(btn_frame, text="2. Search Student", width=22, command=self.search_student).grid(row=0, column=1, padx=5, pady=3)
        tk.Button(btn_frame, text="3. Remove Student", width=22, command=self.remove_student).grid(row=1, column=0, padx=5, pady=3)
        tk.Button(btn_frame, text="4. Display All Students", width=22, command=self.display_all).grid(row=1, column=1, padx=5, pady=3)
        tk.Button(btn_frame, text="5. Enroll in Course", width=22, command=self.enroll_student).grid(row=2, column=0, padx=5, pady=3)
        tk.Button(btn_frame, text="6. Update Grade", width=22, command=self.update_grade).grid(row=2, column=1, padx=5, pady=3)
        tk.Button(btn_frame, text="7. Display Average", width=22, command=self.display_average).grid(row=3, column=0, padx=5, pady=3)
        tk.Button(btn_frame, text="8. Exit", width=22, command=self.exit_app).grid(row=3, column=1, padx=5, pady=3)

        output_frame = tk.LabelFrame(window, text="System Output", padx=10, pady=10)
        output_frame.pack(fill="both", expand=True, padx=15, pady=10)

        self.output_text = tk.Text(output_frame, height=10, state="disabled")
        self.output_text.pack(fill="both", expand=True)

    '''
    Below are all the callback functions used in the buttons and helper(s)
    '''

    # Display end output
    def show_output(self, message):
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, message)
        self.output_text.config(state="disabled")

    # Clears all entry elements
    def clear_inputs(self):
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.course_entry.delete(0, tk.END)
        self.grade_entry.delete(0, tk.END)

    # gets input and checks
    def get_valid_grade(self):
        raw_grade = self.grade_entry.get().strip()
        try:
            grade = float(raw_grade)
            if 0 <= grade <= 100:
                return grade
            messagebox.showerror("Invalid Grade", "Please enter a number between 0 and 100.")
            return None
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a numeric grade.")
            return None

    def add_student(self):
        student_id = self.id_entry.get().strip()
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()

        if not student_id or not name or not email:
            messagebox.showerror("Error", "Student ID, name, and email cannot be empty.")
        elif self.system.add_student(student_id, name, email):
            messagebox.showinfo("Success", "Student added successfully!")
            self.show_output(f"Added Student:\nID: {student_id} | Name: {name} | Email: {email}")
            self.clear_inputs()
        else:
            messagebox.showerror("Error", f"A student with ID '{student_id}' already exists.")

    def search_student(self):
        student_id = self.id_entry.get().strip()
        student = self.system.find_student_from_id(student_id)
        if student:
            self.show_output(student.get_info())
        else:
            messagebox.showerror("Not Found", f"Student with ID '{student_id}' not found.")

    def remove_student(self):
        student_id = self.id_entry.get().strip()
        if self.system.remove_student(student_id):
            messagebox.showinfo("Success", "Student removed successfully!")
            self.show_output(f"Student with ID '{student_id}' was removed.")
            self.clear_inputs()
        else:
            messagebox.showerror("Not Found", f"Student with ID '{student_id}' not found.")

    def display_all(self):
        students = self.system.get_all_students()
        if not students:
            self.show_output("No students are currently in the system.")
        else:
            lines = ["All Enrolled Students:"]
            for student in students:
                lines.append(f"ID: {student.id} | Name: {student.name} | Email: {student.email}")
            self.show_output("\n".join(lines))

    def enroll_student(self):
        student_id = self.id_entry.get().strip()
        student = self.system.find_student_from_id(student_id)
        if not student:
            messagebox.showerror("Not Found", f"Student with ID '{student_id}' not found.")
            return

        course = self.course_entry.get().strip().upper()
        if not course:
            messagebox.showerror("Error", "Course Code cannot be empty.")
            return

        grade = self.get_valid_grade()
        if not grade and grade != 0.0:
            return

        if self.system.enroll_student(student_id, course, grade):
            messagebox.showinfo("Success", "Course added successfully!")
            self.show_output(student.get_info())
            self.clear_inputs()
        else:
            messagebox.showerror("Error", f"Student is already enrolled in {course}. Use Option 6 to update the grade.")

    def update_grade(self):
        student_id = self.id_entry.get().strip()
        student = self.system.find_student_from_id(student_id)
        if not student:
            messagebox.showerror("Not Found", f"Student with ID '{student_id}' not found.")
            return

        course = self.course_entry.get().strip().upper()
        if course not in student.courses:
            messagebox.showerror("Error", f"{student.name} is not enrolled in {course}.")
            return

        grade = self.get_valid_grade()
        if not grade and grade != 0.0:
            return

        self.system.update_grade(student_id, course, grade)
        messagebox.showinfo("Success", "Grade updated successfully!")
        self.show_output(student.get_info())
        self.clear_inputs()

    def display_average(self):
        student_id = self.id_entry.get().strip()
        student = self.system.find_student_from_id(student_id)
        if student:
            avg = self.system.get_student_average(student_id)
            self.show_output(f"Student Name: {student.name}\nAverage Grade: {avg:.1f}")
        else:
            messagebox.showerror("Not Found", f"Student with ID '{student_id}' is not in the system.")

    def exit_app(self):
        messagebox.showinfo("Bye", "Thanks for using the Student Course Management System.")
        self.window.destroy()

if __name__ == "__main__":
  window = tk.Tk()
  app = StudentManagementGUI(window)
  window.mainloop()
