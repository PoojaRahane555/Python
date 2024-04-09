# File handling:
# three modes ==>  read, write, append(to add extra in previous file)

# Write:
f = open('info1.txt','w');               #creation of object
number = input("Enter the number: ")     #taking input from user
f.write(number)                         #writing to the file
f.close()                               #closing the file-mandatory

# Read:
f = None
try:
    fileName = input("Enter the fileName: ")
    f = open('info1.txt','r')
    number = f.read()
    print(number)
except FileNotFoundError:
    print("File not found")
finally:
    if f is not None:
        f.close()

print("Bye EveryOne....")

# Program 1:
f1 = open("info2.txt",'w')
str = input("Enter your Name: ")
f1.write(str)
f1.close()

# program 2:
str = input('Enter your file name: ')
f1 = open('info2.txt','r')
str = f1.read()
f1.close()

# Program 3:

f1 = None
try:
    str = input("Please enter your file name: ")
    f1 = open("info2.txt",'r')
    str = f1.read()
    print(str)
except FileNotFoundError:
    print("file not found")
finally:
    if f1 is not None:
        f1.close()

# program 4:
f2 = open('info3.txt','w')
while str != '@':
    str = input("Enter Name: ")
    if str != '@':
        f2.write(str + '\n')
f2.close()
    

