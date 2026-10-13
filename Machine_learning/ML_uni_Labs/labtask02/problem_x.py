import tracemalloc
from collections import namedtuple
from dataclasses import dataclass


def header(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


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
    problem_x()
