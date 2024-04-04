# 1)Compile type error:
# def sub():
# print(3+3)
# sub()

# 2)Run time error:
x = int(input("Enter NumA: "))
y = int(input("Enter NumB: "))

z = x/y
print(z)
print("Words are very important5")

alpha = ["A","B","C","D","E"]
print(alpha)
print(alpha[4])
# print(alpha[6])

# 3)logical error:
def CalculateBonusSalary(amount):
    # return amount + amount * 0.10
    return amount * 0.10
aa = CalculateBonusSalary(100000)
print(aa)

# program 1:
print("Aai")

try:
    a1 = int(input("Enter any number: "))
    a2 = int(input("Enter any number: "))

    a3 = a1/a2
    print(a3)
except Exception:
    print("error occured.....")

print("Baba")

# program 2:
print("Hello Everyone..")

name = ["Pooja","Kavita","Savita","Vinita"]

try:
    l = int(input("Enter numC"))
    m = int(input("Enter numD"))
    n = l/m
    print(n)
    print(name[5])
except ArithmeticError:
    print("Please enter correct number")
except IndexError:
    print("Please enter valid index")
except Exception:
    print("Please provide correct value")

print("Bye Everyone....")

# program 3:
try:
    o = int(input("Num1: "))
    p = int(input("Num2: "))
    q = o/p
    print(q)
except ArithmeticError:
    print("Arithmatic error occured")
finally:
    print("Irrespective try or except i will always execute")

# program 4:
city = ["Mumbai","Pune","Nashik","Banglore","Varanasi"]
try:
    r = int(input("Enter Num-1:  "))
    s = int(input("Enter Num-2:  "))
    t = r/s
    print(t)
    print(city[3])
except ArithmeticError:
    print("Enter correct number")
except IndexError:
    print("Provide correct index no.")
except Exception:
    print("Something went wrong...")
else:
    print("I will run with try block...")
finally:
    print("I will always execute....")
