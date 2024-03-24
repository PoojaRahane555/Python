# instance methods:

class Person:
    # constructor
    def __init__(self,fn,ln):
        # instance variables
        self.firstName = fn
        self.lastName = ln

    # instance method
    def displayName(self):
        print(self.firstName + self.lastName)

    # lastNameUpdate
    def updateName(self,ln):
        self.lastName = ln

vihan = Person('Vihan',"Kumar")
print(vihan.firstName)
print(vihan.lastName)
vihan.displayName()
vihan.updateName('Dube')
vihan.displayName()


# class methods:
class PersonB:
    city = "Mumbai"  

    # constructor
    def __init__(self,fn,ln):
        # instance variables
        self.firstName = fn
        self.lastName = ln

    # instance methods
    def displayName(self):
        print(self.firstName + self.lastName)
    
    # updatemethod
    def updateName(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
    
    # class method
    @classmethod
    def updateCity(cls,ct):
        cls.city = ct

aaru = PersonB("Aarvi","Lokhande")
print(aaru.firstName)
print(aaru.lastName)
print(aaru.city)
aaru.displayName()
aaru.updateName("Avni","Sharma")
aaru.displayName()

avnish = PersonB("Avnish","Valanj")
print(avnish.firstName)
print(avnish.lastName)
print(avnish.city)
avnish.displayName()
avnish.city = "Panvel"
print(avnish.city)
PersonB.updateCity('Pune')

print(aaru.city)
print(avnish.city)

# static method - count no.of objects
class PersonC:
    count = 0
    country = "India"

    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
        PersonC.count = PersonC.count + 1

    def dispalyName(self):
        print(self.firstName + self.lastName)

    # class method
    @classmethod
    def updateCountry(cls,cnty):
        cls.country = cnty

    # static method
    @staticmethod
    def objectCount():
        return PersonC.count
    
chinki = PersonC("Chinki","Sharma")
print(chinki.firstName)
print(chinki.lastName)
print(chinki.country)
print(chinki.count)
chinki.country = "Bharat"
print(chinki.country)

pinki = PersonC("Pinki","Sharma")
print(pinki.firstName)
print(pinki.lastName)
print(pinki.country)
print(pinki.count)

aa = PersonC.objectCount()
print(aa)


