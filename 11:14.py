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
    
    #outputs all info for a student
    def __repr__(self) -> str:
        return "Student: " + self.name + ", " + str(self.homeroom) + ", " + str(self.grades)

    
#returns true or false depending on whether or not the homeroom of two students are the same
def same_homeroom(student1: Student, student2: Student) -> bool:
        return student1.homeroom is student2.homeroom
luke = Student("Luke", 102, [95, 85, 75])
david = Student("David", 102, [95, 85, 75])

print(luke.average())

print(luke.name)
print(luke.homeroom)
print(luke.grades)

print(same_homeroom(david, luke))

print(luke)