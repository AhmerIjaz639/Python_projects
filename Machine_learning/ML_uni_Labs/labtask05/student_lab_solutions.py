import sys
import tracemalloc
from collections import namedtuple
from dataclasses import dataclass


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


class StudentIII:
    pass


def problem_iii():
    header("iii. Type, __dict__ keys and __module__")
    print("Type of Student class:", type(StudentIII))
    print("__dict__ keys:", list(StudentIII.__dict__.keys()))
    print("__module__ value:", StudentIII.__module__)


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


class StudentVIII:
    pass


def problem_viii():
    header("viii. Two instances")
    student1 = StudentVIII()
    student2 = StudentVIII()
    student1.student_id = "V12"
    student1.student_name = "Jean Ahad"
    student1.student_class = "V"
    student2.student_id = "V13"
    student2.student_name = "Sara Khan"
    student2.student_class = "VI"
    for name, obj in (("student1", student1), ("student2", student2)):
        print(f"\nAttributes of {name}:")
        for attr, value in obj.__dict__.items():
            print(f"  {attr}: {value}")


class StudentPlain:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class


N = 100_000


def measure(label, factory):
    tracemalloc.start()
    objs = [factory(i) for i in range(N)]
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"{label:<28} current: {current / 1024 / 1024:7.2f} MB   "
          f"peak: {peak / 1024 / 1024:7.2f} MB   "
          f"per object: {current / N:6.1f}B")
    return current


def problem_ix():
    header("ix. Memory allocation tests (sys.getsizeof + tracemalloc)")
    s = StudentPlain(1, "Ahad", "BCS-4A")
    print("sys.getsizeof(instance)        :", sys.getsizeof(s), "bytes")
    print("sys.getsizeof(instance.__dict__):", sys.getsizeof(s.__dict__), "bytes")
    print("Instance + __dict__ (approx)   :",
          sys.getsizeof(s) + sys.getsizeof(s.__dict__), "bytes")
    print(f"\nCreating {N:,} objects:")
    measure("Plain class (with __dict__)",
            lambda i: StudentPlain(i, "Ahad", "BCS-4A"))


class StudentSlots:
    __slots__ = ("student_id", "student_name", "student_class")

    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class


@dataclass(slots=True)
class StudentDataclass:
    student_id: int
    student_name: str
    student_class: str


StudentTuple = namedtuple("StudentTuple", "student_id student_name student_class")


def problem_x():
    header("x. Reducing memory allocation")
    print(f"Creating {N:,} objects with each technique:\n")
    base = measure("Plain class (baseline)",
                   lambda i: StudentPlain(i, "Ahad", "BCS-4A"))
    slots = measure("__slots__",
                    lambda i: StudentSlots(i, "Ahad", "BCS-4A"))
    dc = measure("@dataclass(slots=True)",
                 lambda i: StudentDataclass(i, "Ahad", "BCS-4A"))
    nt = measure("namedtuple",
                 lambda i: StudentTuple(i, "Ahad", "BCS-4A"))
    print("\nSaving vs plain class:")
    for label, val in (("__slots__", slots),
                       ("dataclass(slots=True)", dc),
                       ("namedtuple", nt)):
        print(f"  {label:<24} {100 * (base - val) / base:5.1f}% less memory")
    print("\nWhy it works:")
    print("  - A plain instance carries a __dict__ (a hash table) per object.")
    print("  - __slots__ replaces it with fixed-offset storage, so no dict.")
    print("  - Trade-off: no dynamic attributes, and no __dict__ on instances.")
    print("  - Strings like 'Ahad' are shared here; the savings come from the")
    print("    object structure, not the data.")


if __name__ == "__main__":
    problem_i()
    problem_ii()
    problem_iii()
    problem_iv()
    problem_v()
    problem_vi()
    problem_vii()
    problem_viii()
    problem_ix()
    problem_x()
