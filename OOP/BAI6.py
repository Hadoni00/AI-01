class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def get_age(self, current_year):
        return current_year - self.birth_year

    def info(self):
        return f"{self.name}, {self.birth_year}"

class Student(Person):
    def __init__(self, name, birth_year, student_id, scores=None):
        super().__init__(name, birth_year)
        self.student_id = student_id
        self.scores = scores if scores else []

    def avg_score(self):
        return sum(self.scores) / len(self.scores) if self.scores else 0

    def rank(self):
        avg = self.avg_score()
        if avg >= 8:
            return "Excellent"
        elif avg >= 6.5:
            return "Good"
        elif avg >= 5:
            return "Average"
        else:
            return "Weak"

    def info(self):
        return f"{super().info()}, ID: {self.student_id}, Avg: {self.avg_score():.2f}, Rank: {self.rank()}"
class Teacher(Person):
    def __init__(self, name, birth_year, teacher_id, subject, salary):
        super().__init__(name, birth_year)
        self.teacher_id = teacher_id
        self.subject = subject
        self.salary = salary

    def info(self):
        return f"{super().info()}, ID: {self.teacher_id}, Subject: {self.subject}, Salary: {self.salary}"

class SchoolClass:
    def __init__(self, class_name, homeroom_teacher=None):
        self.class_name = class_name
        self.students = []
        self.homeroom_teacher = homeroom_teacher
    def add_student(self, student):
        self.students.append(student)
    def remove_student_by_id(self, student_id):
        self.students = [s for s in self.students if s.student_id != student_id]

    def find_student_by_name(self, name):
        return [s for s in self.students if s.name == name]

    def class_avg_score(self):
        if not self.students:
            return 0
        return sum(s.avg_score() for s in self.students) / len(self.students)
    def top_student(self):
        if not self.students:
            return None
        return max(self.students, key=lambda s: s.avg_score())

    def sort_by_avg_desc(self):
        self.students.sort(key=lambda s: s.avg_score(), reverse=True)

    def info(self):
        t_info = self.homeroom_teacher.info() if self.homeroom_teacher else "no teacher"
        s_info = "\n".join(s.info() for s in self.students)
        return f"Class: {self.class_name}\nTeacher: {t_info}\nStudents:\n{s_info}"