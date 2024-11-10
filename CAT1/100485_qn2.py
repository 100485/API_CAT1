class Student:
    def __init__(self, student_id: int, name:str):
        self.student_id: int = student_id
        self.name: str = name
        self.assignments: dict[str, float] = {}

    def __str__(self):
        return f"Student ID: {self.student_id} Name: {self.name}"

    def add_assignment_and_grade(self, assignment_name: str, grade: float):
        self.assignments.update({assignment_name: grade})

    def display_grades(self):
        for assignment_name, grade in self.assignments.items():
            print(f"- {assignment_name}: {grade}")

class Instructor:
    def __init__(self, name:str, course_name:str):
        self.name: str = name
        self.course_name: str = course_name
        self.students: list[Student] = []

    def __str__(self):
        return f"Instructor {self.name}, Course: {self.course_name}"

    def add_student_to_course(self, student: Student):
        self.students.append(student)

    def assign_grade_to_student(self, assignment_name: str, grade: float, student: Student):
        found_student = False
        for s in self.students:
            if s.student_id == student.student_id:
                s.add_assignment_and_grade(assignment_name, grade)
                found_student = True
        if found_student == False:
            print(f"{self} has no student {student}!")

    def display_all_students_and_their_grades(self):
        for student in self.students:
            print(student)
            print(student.display_grades())


def main():
    # sample of students
    students = [
        Student(1, "John Kamau"),
        Student(2, "Jane Kamau"),
    ]

    # sample of instructor
    instructor = Instructor("Peter Kamau", "Intro to Programming")

    # Add students to the course
    for student in students:
        instructor.add_student_to_course(student)

    while True:
        print(f"\nWelcome to AMS - {instructor}!")
        print("1. List all students")
        print("2. Record assignment grades")
        print("3. Display grades for all students")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            print("\nStudents in the course:")
            for student in instructor.students:
                print(student)

        elif choice == "2":
            student_id = input("\nEnter the student ID to assign a grade: ")
            student_id = int(student_id.strip())
            student = next((s for s in instructor.students if s.student_id == student_id), None)

            if student:
                assignment_name = input("Enter the assignment name: ")
                try:
                    grade = input("Enter the grade: ")
                    grade = float(grade)
                    instructor.assign_grade_to_student(assignment_name, grade, student)
                    print(f"Grade recorded for {student.name} on '{assignment_name}'.")
                except ValueError:
                    print("Invalid grade. Please enter a numeric value.")
            else:
                print(f"No student found with ID {student_id}.")

        elif choice == "3":
            print("\nGrades for all students:")
            instructor.display_all_students_and_their_grades()

        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
