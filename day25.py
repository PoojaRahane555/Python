# single-level inheritance:
# 1)parent class having constructor and child class without constructor

class Student:
    def __init__(self,fn,ln,adrNo):
        self.firstName = fn
        self.lastName = ln
        self.adharNo = adrNo
    
    def displayName(self):
        print(self.firstName + self.lastName)

# dipak = Student("Dipak","Lokhande",111222333) 
# dipak.displayName()
# print(dipak.adharNo)

class Teacher(Student):
    salary = 100000

    def displaySalary(self):
        print(self.salary)

dipak = Teacher("Dipak","Lokhande",111222333)
dipak.displayName()
dipak.displaySalary()
print(dipak.firstName)
print(dipak.lastName)
print(dipak.adharNo)
print(dipak.salary)

# parent class having constructor and child class also having constructor

class StudentA:

    def __init__(self,fn,ln,adrNo):
        self.firstName = fn
        self.lastName = ln
        self.adharNo = adrNo

    def displayName(self):
        print(self.firstName + self.lastName)
    
class TeacherA(StudentA):

    def __init__(self, fn, ln, adrNo,slry):
        super().__init__(fn, ln, adrNo)
        self.salary = slry

    def displaySalary(self):
        print(self.salary)

kavita = TeacherA("Kavita","Rahane",123456789,500000)
kavita.displayName()
kavita.displaySalary()
print(kavita.firstName)
print(kavita.lastName)
print(kavita.adharNo)
print(kavita.salary)

# multi-level-inheritance:

class StudentB:

    def __init__(self,fn,ln,adrNo):
        self.firstName = fn
        self.lastName = ln
        self.adharNo = adrNo

    def displayName(self):
        print(self.firstName + self.lastName)

class TeacherB(StudentB):

    def __init__(self, fn, ln, adrNo,slry):
        super().__init__(fn, ln, adrNo)
        self.salary = slry

    def displaySalary(self):
        print(self.salary)

class Professor(TeacherB):

    def __init__(self, fn, ln, adrNo, slry,speczn):
        super().__init__(fn, ln, adrNo, slry)
        self.specialization = speczn

    def displaySpecialization(self):
        print(self.specialization)

shradha = Professor("Shradha","Dayma",112233445566,250000,"Botany")
shradha.displayName()
shradha.displaySalary()
shradha.displaySpecialization()

print(shradha.firstName)
print(shradha.lastName)
print(shradha.adharNo)
print(shradha.salary)
print(shradha.specialization)









