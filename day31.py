# Exception:

# A single try block can be followed by several except block.
# Multiple except blocks can be used to handle multiple excpetions. 
# We cannot write except block without try block.
# We cannot write try block without except block.
# Else block and finally block are not compulsory.
# When there is no exception raised else block is executed after try block.
# Finally block is always executed.

# Program 1:
print("Good Morning")
try:
    city = ["Panvel","Pune","Nashik","Banglore"]
    a = int(input("Please Enter NumberA"))
    b = int(input("Please Enter NumberB"))
    print(a/b)
    print(city[5])
except ArithmeticError:
    print("Please Enter correct Number")
except IndexError:
    print("Please provide correct index number")
except Exception:
    print("Something went wrong")

print("Good Night")

# Program 2:
print("hello")
# try:
#     print(56/0)
# finally:
#     print("I will always execute")   #zero division error occurs still executed
print("bye")

# Program 3:
print(".......Program3.............")
def CalculateAvg(list):
    total = 0
    for item in list:
        total = total + 1
    avg = total/len(list)
    return total , avg

try:
    t,a = CalculateAvg([1,2,3,4,5,6])
    print(t)
    print(a)
except TypeError:
    print("Please enter correct input")
except ZeroDivisionError:
    print("Please provide atleast one value")
except Exception:
    print("Something went wrong")

# Program 4:
print("come")
try:
    z = 10
    assert z > 1 and z <= 10
    print(z)
except AssertionError:
    print("condition not matched")

print("Go")

