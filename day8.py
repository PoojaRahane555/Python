# List:

number = [11,22,33,44]
print(number)

number2 = number 
number2[2] = 35
print(number2)
print(number)

# list methods:
# 1)Append: Add the element at the last of list

name = ["Pooja","Savita","Kavita","Babita"]
print(name)
name.append("Sarita")
# print(name)

# 2a)Pop: removes the last element
name.pop()
print(name)

# 2b)Pop(index): removes the element index-wise
# name.pop(1)
# print(name)

# 2c)Remove: removes the element by name
name.remove("Kavita")
print(name)

# 3)Clear: clear the all data from list
name.clear()
print(name)


# 4)Count: gives the count of specific element 
color = ["baby-pink","baby blue","mint","peach","purple","maroon","mint"]
print(color)
a =color.count("mint")
print(a)

# 5)Reverse: gives reverse order of element
color.reverse()
print(color)

# 6)Sort: Alphabatically sort out element
color.sort()
print(color)

# 7)Insert: Replace the element index-wise
color.insert(3,"lavendar")
print(color)

# 8)IN: if element is present gives true otherwise false
aa = "peach" in color
print(aa)
print(".........................................")
# program 1:
# same output comes for both bcz.only address changed memory location is same for both.
numA = [1,2,3]
numB = numA
numB[1] = 22
print(numA)
print(numB)

# program 2:
# copy method changes the memory location so output comes different for both
numC = [11,22,33,44]
numD = numC.copy()
numD[2] = 333
print(numD)
print(numC)

# program 3:
# Add the all element from another list
city1 = ["mumbai","pune","ujjain"]
city2 = ["banglore","singapore","dhule"]
city1.extend(city2)
print(city1)

# program 4:
birthYear = [1998,1999,2000,2001]
age = []
for x in birthYear:
    # print(x)
    # print(2024 - x)
    age.append(2024 - x)
print(age)

score = [20,45,65,80,30,98]
above50 = []
for x1 in score:
    # print(x1)
    if x1 > 50:
        above50.append(x1)

print(above50)

count = [10,20,30,40,50]
total = 0
for x in count:
    # print(x)
    total = total + x
print(total)

student = ["Aarvi","Aadvi","Janvi","Sanvi","Kanvi"]
for x in student:
    print("Hello " + x)
    






