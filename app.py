class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.students = []

    def set_password(self, password):
        self.password = password

    def check_password(self, password):
        return self.password == password

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = {}

    def add_grade(self, course, grade):
        self.grades[course] = grade

    def update_grade(self, course, grade):
        if course in self.grades:
            self.grades[course] = grade

    def delete_grade(self, course):
        if course in self.grades:
            del self.grades[course]

    def get_average_grade(self):
        if self.grades:
            return sum(self.grades.values()) / len(self.grades)
        return 0

class PerformanceReport:
    def __init__(self, student):
        self.student = student

    def generate_report(self):
        report = f"Performance Report for {self.student.name}:\n"
        report += "\n".join([f"{course}: {grade}" for course, grade in self.student.grades.items()])
        report += f"\nAverage Grade: {self.student.get_average_grade()}"
        return report

class StudentPerformanceSystem:
    def __init__(self):
        self.users = []
        self.students = []

    def sign_up(self, username, password):
        user = User(username, password)
        self.users.append(user)
        return user

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.check_password(password):
                return user
        return None

    def add_student(self, user, student_id, name):
        if user in self.users:
            student = Student(student_id, name)
            user.students.append(student)
            self.students.append(student)
            return ""
        return None

    def update_student(self, user, student_id, name):
        if user in self.users:
            for student in self.students:
                if student.student_id == student_id:
                    student.name = name
                    return student
        return None

    def delete_student(self, user, student_id):
        if user in self.users:
            for student in self.students:
                if student.student_id == student_id:
                    self.students.remove(student)
                    user.students.remove(student)
                    return student
        return None

