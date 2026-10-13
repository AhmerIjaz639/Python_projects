def header(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


class StudentVII:
    student_id = "V12"
    student_name = "Jean Ahad"


def display_attributes(cls):
    for key, value in vars(cls).items():
        if not key.startswith("__"):
            print(f"{key} -> {value}")


def problem_vii():
    header("vii. Display function")
    StudentVII.student_class = "V"
    display_attributes(StudentVII)


if __name__ == "__main__":
    problem_vii()
