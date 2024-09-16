class Grade:
    def __init__(self, assignment, grade):
        self._assignment = assignment
        self._grade = grade

    def get_assignment(self):
        return self._assignment

    def get_grade(self):
        return self._grade