def header(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def problem_i():
    header("i. Instance namespace")

    class Student:
        def __init__(self, student_id, student_name):
            self.student_id = student_id
            self.student_name = student_name

    s = Student(101, "Ahad")
    print("Instance:", s)
    print("Namespace (s.__dict__):", s.__dict__)


if __name__ == "__main__":
    problem_i()
