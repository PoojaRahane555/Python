# class:
# program 1:
class Person:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
    
    def displayName(self):
        print(self.firstName + self.lastName)

aarvi = Person("Aarvi","Lokhande")
print(aarvi.firstName)
print(aarvi.lastName)
aarvi.displayName()

vedant = Person("Vedant","Sharma")
vedant.displayName()
vedant.firstName = "Ved"
print(vedant.firstName)

# program 2:
class Person1:
    country = "Hindustan" 

    def __init__(self,fn,ln):
        self.first_name = fn
        self.last_name =ln
    
    def displayName(self):
        print(self.first_name + self.last_name)

    @classmethod
    def changeCountry(cls,cntry):
        cls.country = cntry

ruchi = Person1("Ruchi","Sawant")
priya = Person1("Priya","More")
neel = Person1("Neel","Rode")

ruchi.displayName()
priya.displayName()
print(ruchi.country)
print(priya.country)

ruchi.country = "India"
print(ruchi.country)
print(priya.country)
print(neel.country)

Person1.changeCountry("Bharat")
print(ruchi.country)
print(priya.country)
print(neel.country)

