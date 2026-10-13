def header(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


class Student:
    pass


class Marks:
    pass


def problem_iv():
    header("iv. isinstance / issubclass")
    student1 = Student()
    marks1 = Marks()
    print("student1 is instance of Student:", isinstance(student1, Student))
    print("student1 is instance of Marks  :", isinstance(student1, Marks))
    print("marks1   is instance of Student:", isinstance(marks1, Student))
    print("marks1   is instance of Marks  :", isinstance(marks1, Marks))
    print("Student is subclass of object:", issubclass(Student, object))
    print("Marks   is subclass of object:", issubclass(Marks, object))


if __name__ == "__main__":
    problem_iv()
