class Assignment:
    def __init__(self, name, max_points, due_date):
        self._name = name
        self._max_points = max_points
        self._due_date = due_date

    def get_name(self):
        return self._name

    def get_max_points(self):
        return self._max_points

    def get_due_date(self):
        return self._due_date