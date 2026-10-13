def header(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


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


if __name__ == "__main__":
    problem_viii()
