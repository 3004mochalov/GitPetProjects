from Person import Person

class Student(Person):
    def __init__(self, first, second, year, grade, diary):
        super().__init__(first, second, year)
        self.grade = grade
        self.diary = diary
    
    def addMark(self, subject, mark, date):
        self.diary[subject][date] = mark
    
    def getMarks(self, subject):
        return self.diary[subject]
    
    def printAll(self):
        pprint.pprint(self.diary)
    
    def __str__(self) -> str:
        return self.firstname + ' ' + self.lastname + ' Age: ' + self.age + ' Grade: ' + self.grade