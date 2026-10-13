def header(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def student_data(student_id, student_name=None, student_class=None):
    print("Student ID:", student_id)
    if student_name:
        print("Student Name:", student_name)
    if student_class:
        print("Student Class:", student_class)


def problem_ii():
    header("ii. student_data()")
    student_data(1)
    print("--")
    student_data(2, student_name="Ali")
    print("--")
    student_data(3, student_class="BCS-4A")
    print("--")
    student_data(4, student_name="Sara", student_class="BCS-4B")


if __name__ == "__main__":
    problem_ii()
