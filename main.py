import csv

from Assignment import Assignment
from Student import Student


def main():
    students = []
    assignments = []

    # Read grades from a CSV fileW
    csv_file = '/Users/davidgood/projects/Walsh/students.csv'

    try:
        with open(csv_file, mode='r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            for header in headers[1:]:
                assignments.append(Assignment(header, 100, "2024-09-30"))  # Dummy due date

            for row in reader:
                student_name = row[0]
                student = Student(student_name, student_name.lower())  # Simulating ID as lower-case name
                for i, grade in enumerate(row[1:]):
                    student.add_grade(assignments[i], int(grade))
                students.append(student)

    except FileNotFoundError:
        print(f"File {csv_file} not found.")

    # Display students and their average grades
    for student in students:
        print(f"{student.get_name()}: {student.calculate_average_grade()}")

def calculate_average_grade(students, assignment):
    total = 0
    count = 0
    for student in students:
        grade = student.get_grade(assignment)
        if grade is not None:
            total += grade
            count += 1
    return total / count if count > 0 else 0


if __name__ == "__main__":
    main()