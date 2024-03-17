# integer as a parameter and integer as a return type:
def Multiply(x,y):
    return x * y
aa = Multiply(5,6)
print(aa)

# float as parameter and float as return type:
def divide(x,y):
    return x/y
bb = divide(55.5,33.2)
print(bb)

# boolean as parameter and boolean as return type:
def canDrive(age,vehicle):
    if age > 18 and vehicle:
        return True
    else:
        return False
cc = canDrive(22,True)
print(cc)

# string as parameter and string as return type:
def greet(name):
    return "Hello "  + name
dd = greet("Tanmay")
print(dd)

# list as parameter and list as return type:
alpha = ["a","b","c","d"]

def Add(lst):
    lst.append("e")
    return lst
ee = Add(alpha)
print(ee)
    
# dictionary as parameter and dictionary as return type:
info = {
    "first_name" : "Kanvi",
    "last_name"  : "Lokhande"
}
print(info)

def Addprop(dic):
    dic["city"] = "Panvel"
    return dic
ff = Addprop(info)
print(ff)

# tuple as a parameter and tuple as a return type:
tupleA = ("mango","banana","orange")
print(tupleA)

def addElement(tupC):
    tupC = list(tupC)
    tupC.append("apple")
    tuple(tupC)
    return tupC
gg = addElement(tupleA)
print(gg)

# set as parameter and set as return type:
all = {"fruits","flowers","animal","vehicle"}

def addEle(setB):
    setB.add("birds")
    return setB 
hh = addEle(all)
print(hh)