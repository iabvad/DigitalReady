class Student:
    def __init__(self, name: str, homeroom: int, grades: list[float]) -> None:
        self.name = name
        self.homeroom = homeroom
        self.grades = grades

luke = Student("Luke", 102, [95, 85, 75])

print(luke.name)
print(luke.homeroom)
print(luke.grades)