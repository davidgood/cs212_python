from Grade import Grade


class Student:
    def __init__(self, name, student_id):
        self._name = name
        self._id = student_id
        self._grades = []

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id

    def add_grade(self, assignment, grade):
        self._grades.append(Grade(assignment, grade))

    def get_grade(self, assignment):
        for grade in self._grades:
            if grade.get_assignment() == assignment:
                return grade.get_grade()
        return None

    def calculate_average_grade(self):
        if not self._grades:
            return 0
        total = sum(grade.get_grade() for grade in self._grades)
        return total / len(self._grades)

    def simulate_api_post(self):
        print(f"Simulating Posting student data to external system:")
        print(f"Student Name: {self._name}")
        print(f"Student ID: {self._id}")
        for grade in self._grades:
            print(f"Assignment: {grade.get_assignment().get_name()} Grade: {grade.get_grade()}")