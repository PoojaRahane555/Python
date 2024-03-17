# TUPLE:
nums = [11,22,33,44]
print(nums)
print(type(nums))
print(nums[2])
nums[3] = 444
print(nums)

# in tuple can not update element
# tuple stores value by index
tupleC = ("flowers","fruits","vehicle","names","numbers")
print(tupleC)
print(type(tupleC))
print(tuple[1])
# tuple[2] = "animal"
# print(tupleC)

# TUPLE-LOOP:
names = ("Pooja","Kavita","Babita","Savita")

for x in names:
    print(x)

for x in range(len(names)):
    print(names[x])

for x in range(4):
    print(names[x])

for x in range(3,-1,-1):
    # print(x)
    print(names[x])

fruits = ("mango","apple","banana","custardapple","strawberry")
x1 = 0
while(x1 < len(fruits)):
    # print(x1)
    print(fruits[x1])
    x1 = x1 + 1

x2 = 4
while(x2 >= 0):
    # print(x2)
    print(fruits[x2])
    x2 = x2 - 1

# program 1:
# class integer
num2 = 11
print(num2) 
print(type(num2))

# class tuple
num3 = 55,
print(num3)
print(type(num3))
print(num3[0])

# program 2
color = ("red","yellow","orange","baby-pink")
print(color)

a,b,c,d = color
print(a)
print(b)
print(c)
print(d)

# program 4
# count: count the repetative element and return total no.of repetative element
vehicle = ("audi","sedane","audi","mercedes","Audi")
print(vehicle)
aa = vehicle.count("audi")
print(aa)

# program 5 
# Index: gives the index of given element
bb = vehicle.index("Audi")
print(bb)

# program 6:
# IN: gives the boolean value for given element
furniture = ("cupboard","chair","table")
print("chair" in furniture)

# program 7
alpha = ("A","B","C","D")
print(alpha)
print(type(alpha))
print(len(alpha))

aaa = list(alpha)
print(aaa)
aaa.append("E")
bbb = tuple(aaa)
print(bbb)


