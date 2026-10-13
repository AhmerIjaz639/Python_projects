def header(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


class StudentIII:
    pass


def problem_iii():
    header("iii. Type, __dict__ keys and __module__")
    print("Type of Student class:", type(StudentIII))
    print("__dict__ keys:", list(StudentIII.__dict__.keys()))
    print("__module__ value:", StudentIII.__module__)


if __name__ == "__main__":
    problem_iii()
