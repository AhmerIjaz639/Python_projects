import sys
import tracemalloc


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


if __name__ == "__main__":
    problem_ix()
