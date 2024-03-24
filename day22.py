# Class:
# program 1

class Person:
    first_name = "Pooja"
    last_name  = "Lokhande"

    def walk(self):
        print("I am walking")
    
    def talk(self):
        print("I am talking")

pooja = Person()
print(pooja.first_name)
print(pooja.last_name)
pooja.walk()
pooja.talk()

kanvi = Person()
print(kanvi.first_name)
print(kanvi.last_name)
kanvi.walk()
kanvi.talk()

kanvi.first_name = "Kanvi"
kanvi.last_name = "Rahane"
print(kanvi.first_name)
print(kanvi.last_name)


# program 2:

class PersonA:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
    
    def walk(self):
        print("I am walking")

    def talk(self):
        print("I am talking")

dipak = PersonA('Dipak',"Lokhande")
print(dipak.firstName)
print(dipak.lastName)
dipak.walk()
dipak.talk()

vihan = PersonA("Vihan","Sharma")
print(vihan.firstName)
print(vihan.lastName)
vihan.walk()
vihan.talk()
vihan.city = "Belapur"

class Vehicle:
    def __init__(self,ty,mo):
        self.type = ty
        self.model = mo
    
    def start(self):
        print("I am starting the vehicle")
    
    def stop(self):
        print("I am stoping the vehicle")

audi = Vehicle("Audi","e-tron")
print(audi.model)
print(audi.type)
audi.start()
audi.stop()
audi.color = "white"
print(audi.color)
        





