# SET:
# allow duplicate value to store in set but does not consider in return form
# can not update value
# does not store value by index

setA = {11,12,13,14,15}
print(setA)
print(len(setA))
print(type(setA))

setB = {1,2,3,2,4,5}
print(setB)
print(len(setB))

# for loop:
for x in setB:
    print(x)

# Methods:
# 1)ADD:
setC = {"pooja","aarvi","kanvi"}
print(setC)
setC.add("kanchan")
print(setC)

# POP:
aa = setC.pop()
print(aa)
print(setC)

setC.remove("pooja")
print(setC)



