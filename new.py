class Student:
    def __init__(self, name: str, homeroom: int, grades: list[float]) -> None:
        self.name = name
        self.homeroom = homeroom
        self.grades = grades
    
    #returns the average of all values inside of the grades list
    def average(self) -> float:
        x = 0
        for i in self.grades:
            x += i
        return (x/len(self.grades))
    
luke = Student("Luke", 102, [95, 85, 75])
print(luke.average())