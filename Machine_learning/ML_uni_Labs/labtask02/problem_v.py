def header(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


class StudentV:
    student_name = "Ahad"
    marks = 80


def problem_v():
    header("v. Modify attribute values")
    print("Original values:")
    print("student_name:", StudentV.student_name)
    print("marks:", StudentV.marks)
    StudentV.student_name = "Ali"
    StudentV.marks = 95
    print("\nModified values:")
    print("student_name:", StudentV.student_name)
    print("marks:", StudentV.marks)


if __name__ == "__main__":
    problem_v()
