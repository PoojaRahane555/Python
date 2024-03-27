# INHERITANCE:

# 1) Single-level inheritance:

class Father:
    def __init__(self,fn,ln,ct):
        self.firstName = fn
        self.lastName = ln
        self.city = ct

    def displayName(self):
        print(self.firstName + self.lastName)

class Son(Father):
    def __init__(self, fn, ln, ct,sfn):
        super().__init__(fn, ln, ct)
        self.sname = sfn

    def displaySname(self):
        print(self.sname + self.lastName)
        
sachin = Son("Sachin","Rode","Mumbai","Avi")
sachin.displayName()
sachin.displaySname()
print(sachin.firstName)
print(sachin.lastName)
print(sachin.city)
print(sachin.sname)

# 2)Multi-level inheritance:

class GrandFather:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def displayGname(self):
        print(self.firstName + self.lastName)


class Father(GrandFather):
    def __init__(self, fn, ln,ffn):
        super().__init__(fn, ln)
        self.fname = ffn

    def displayFname(self):
        print(self.fname + self.lastName)

class Daughter(Father):
    def __init__(self, fn, ln, ffn,dfn):
        super().__init__(fn, ln, ffn)
        self.dname = dfn

    def displayDname(self):
        print(self.dname + self.lastName)

rasika = Daughter("Mukesh","Valanj","Nilesh","Rasika")
rasika.displayGname()
rasika.displayFname()
rasika.displayDname()
print(rasika.firstName)
print(rasika.lastName)
print(rasika.fname)
print(rasika.dname)

# 3)Herarchical inheritance:

class Mother:
    def __init__(self,fn,ln):
        self.first_name = fn
        self.last_name = ln
    
    def displayMname(self):
        print(self.first_name + self.last_name)

class Son(Mother):
    def __init__(self, fn, ln,sfn):
        super().__init__(fn, ln)
        self.sname = sfn

    def displaySname(self):
        print(self.sname + self.last_name)

class Daughter(Mother):
    def __init__(self, fn, ln,dfn):
        super().__init__(fn, ln)
        self.dname = dfn

    def displayDname(self):
        print(self.dname + self.last_name)

sidhu = Son("Sneha","Shinde","Sidharth")
sidhu.displayMname()
sidhu.displaySname()
print(sidhu.first_name)
print(sidhu.last_name)
print(sidhu.sname)

sayli = Daughter("Sneha","Shinde","Sayli")
sayli.displayMname()
sayli.displayDname()
print(sayli.first_name)
print(sayli.last_name)
print(sayli.dname)


# 4)Multi-level Inheritance:

class Mother:

    def __init__(self,fn,ln):
        print("Mother constructor is called....")
        self.firstName = fn
        self.lastName = ln

    def displayName(self):
        print(self.firstName + self.lastName)

class Father:

    def __init__(self,fn,ln):
        print("Father constructor is called...........")
        self.firstName = fn
        self.lastName = ln

    def displayName(self):
        print(self.firstName + self.lastName)

class Daugher(Mother,Father):

    def __init__(self, fn, ln, dfn):
        super().__init__(fn, ln)
        self.dname = dfn

    def displayDname(self):
        print(self.dname + self.lastName)

pooja = Daugher("Ranjana","Rahane","Pooja")
pooja.displayDname()
pooja.displayName()
print(pooja.firstName)
print(pooja.lastName)
print(pooja.dname)