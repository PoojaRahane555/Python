# Custom Error i.e Raising Exception:

x = int(input("Please enter numberA:"))
y = int(input("Please enter numberB:"))
print(x)
print(y)

if x % 2 == 0:
    print("Even number")
else:
    print("Odd number")

z = int(input("Please enter num"))
if z % 2 == 0:
    print("number entered is even")
else:
    print("enter even number only")

# raising exception:
# aa = int(input("Please enter the number"))

# if aa % 2 != 0:
#     raise Exception("works with only even number")
# else:
#     print("please enter correct input")

# calculating age:
current_year = 2024
born_year = 1998
age = current_year - born_year
print(age)

# negative age:
year = 2020
bornYear = 2030
currentAge = year - bornYear
# print(currentAge)

# if bornYear > year:
#     raise Exception("Please enter valid year")
# else:
#     print(currentAge)

# converting logic into fuction:
def calculateAge(birthYear):
    currentY = 2024
    if  birthYear > currentY:
        raise Exception("Please enter corret year")
    else:
        age = currentY - birthYear
        print(age)
# calculateAge(2000)

try:
    calculateAge(2002)
except:
    print("something went wrong...") 
    
print("hello world")
