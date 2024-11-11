
class Student:
    def Details (self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade

    def display_grades(self):
        print(f"Grades for {self.name} ({self.student_id}):")
        for assignment, grade in self.assignments.items():
            print(f"{assignment}: {grade}")


class Instructor:
    def Details(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def assign_grade(self, student, assignment_name, grade):
        if student in self.students:
            student.add_assignment(assignment_name, grade)

    def display_all_students_grades(self):
        print(f"Grades for {self.course_name}:")
        for student in self.students:
            student.display_grades()



def main():
    instructor = Instructor("Dr. Smith", "Math 101")
    student1 = Student("Alice", "S001")
    instructor.add_student(student1)
    instructor.assign_grade(student1, "Assignment 1", 90)
    instructor.display_all_students_grades()

if __name__ == "__main__":
    main()
