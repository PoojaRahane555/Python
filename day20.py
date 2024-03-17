# list comprehension:
# program 1: print age according to their years
year = [1998,1999,2000,2001]
age = []
for x in year:
    age.append(2024 - x)
print(age)

a1 = [2024-x for x in year]
print(a1)

# program 2: print sqauare of all numbers
num = [1,2,3,4,5,6,8,7,9,10]
a2 = [ x*x for x in num]
print(a2)

# program 3: print even numbers 
a3 = [ x for x in num if x % 2 == 0]
print(a3)

# program 4: print odd numbers
a4 = [x for x in num if x % 2 != 0]
print(a4)

# program 5: print odd and even 
number = [1,2,3,4,5,6]
a5 = ["even" if x % 2 == 0 else "odd" for x in number]
print(a5)

# program 6: print name which have length greater than 6
student = ["Kartiki","Rajnandini","aarvi","Prisha","Vidhi","Suchita"]
a6 = [x for x in student if len(x) > 6]
print(a6)




