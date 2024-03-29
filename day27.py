# Polymorphism:
# A)Overloading: Which is not possible in Python
# same class, same method name , different signature

# program 1:

class Calculator:

    def addition(self,a,b):
        print(a+b)
    
    def addition(self,a,b,c):
        print(a+b+c)
    
    def addition(self,a,b,c,d):
        print(a+b+c+d)

alpha = Calculator()
# alpha.addition(11,22)
# alpha.addition(11,22,33)
alpha.addition(11,22,33,44)

class Calculator2:

    def addition(self,l = None, m = None, n = None, o = None):

        if l != None and m != None and n != None and o != None:
            print(l + m + n + o)
        elif l != None and m != None and n != None:
            print(l + m + n)
        elif l != None and m != None:
            print(l + m)

alpha2 = Calculator2()
alpha2.addition(10,20)
alpha2.addition(10,20,30)
alpha2.addition(10,20,30,40)

# program 2:
class Cat:
    def talk(self):
        print('Meows Meows')

class Human:
    def talk(self):
        print('Good Morning')

Kittu = Cat()
Aarvi = Human()

def call_talk(obj):
    obj.talk()

call_talk(Kittu)
call_talk(Aarvi)

# Program2:
class Dog:
    def talk(self):
        print("Bow Bow")

class Human:
    def talk(self):
        print("Hello Everyone")

class Duck:
    def sound(self):
        print("Quack Quack")

x = Dog()
y = Human()
z = Duck()

def call_talk(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    else:
        obj.sound()

call_talk(x)
call_talk(y)
call_talk(z)

# ......................................///..........................
# program 3: Operator OverLoading
print(5 + 5)
print(6 > 5)
print("x" + "y")
print(['a','b'] + ['c','d'])

class BookA:

    def __init__(self,pages):
        self.pages = pages

    def __add__(self,other):
        return self.pages + other.pages

class BookB:

    def __init__(self,pages):
        self.pages = pages

    def __add__(self,other):
        return self.pages + other.pages

Geeta = BookA(500)
Haripath = BookB(100)

print(Geeta.pages + Haripath.pages)
print(Geeta.pages > Haripath.pages)
print(Geeta + Haripath)
print(Haripath + Geeta)

# 
class BookC:

    def __init__(self,pages):
        self.pages = pages

    def __gt__(self,other):
        return self.pages > other.pages

class BookD:

    def __init__(self,pages):
        self.pages = pages
    
    def __gt__(self,other):
        return self.pages > other.pages

Shivpuran = BookC(400)
Tulsipuran = BookD(300)
print(Shivpuran.pages + Tulsipuran.pages)
print(Shivpuran.pages < Tulsipuran.pages)
print(Shivpuran > Tulsipuran)
print(Tulsipuran > Shivpuran)

# B)Overriding: different class, same method name, same signature

class WorldBank:

    def save(self):
        print('I am save from WorldBank')
    
    def loan(self):
        print('I am loan from WorldBank')

class HDFC(WorldBank):

    def save(self):
        super().save()
        print('I am save from HDFC bank')
    
    def loan(self):
        super().loan()
        print('I am loan from HDFC bank')

bank1 = HDFC()
bank1.save()
bank1.loan()

class ICICI(WorldBank):

    def save(self):
        print('I am save from ICICI bank')

    def loan(self):
        print('I am loan from ICICI bank')

bank2 = ICICI()
bank2.save()
bank2.loan()




    
