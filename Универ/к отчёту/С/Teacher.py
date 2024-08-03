from Student import Student

class Teacher(Student):
    def __init__(self, first, second, year, grade, diary, auditorium, subjects):
        super().__init__(first, second, year, grade, diary)
        self.auditorium = auditorium
        self.subjects = subjects
    
    def setAuditorium(self, new_aud):
        self.auditorium = new_aud
    
    def addSubject(self, grade, subject):
        self.auditorium[grade].append(subject)
    
    def delSubject(self, grade, subject):
        self.auditorium[grade].remove(subject)
    
    def __str__(self) -> str:
        temp = []
        for i in self.subjects.values():
            for j in i:
                temp.append(j)
        temp = set(temp)
        return self.firstname + ' ' + self.lastname + ' Age: ' + self.age + ' Auditorium: ' + self.auditorium + ' ' + ' '.join(temp)