def header(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


class StudentVI:
    student_id = "V12"
    student_name = "Jean Ahad"


def show_class_attrs(cls):
    for key, value in vars(cls).items():
        if not key.startswith("__"):
            print(f"{key} = {value}")


def problem_vi():
    header("vi. Add and delete attributes")
    print("Original attributes:")
    show_class_attrs(StudentVI)
    StudentVI.student_class = "V"
    print("\nAfter adding student_class:")
    show_class_attrs(StudentVI)
    del StudentVI.student_name
    print("\nAfter removing student_name:")
    show_class_attrs(StudentVI)


if __name__ == "__main__":
    problem_vi()
