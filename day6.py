# While loop:
# initialization
# while(condition):
# statement
# increment or decrement

# print zero to five:
x1 = 0
while(x1 <= 5):
    print(x1)
    x1 = x1 + 1

# print 91 to 100:
x2 = 91
while(x2 <= 100):
    print(x2)
    x2 = x2 + 1

# print table of three:
x3 = 3
while(x3 <= 30):
    print(x3)
    x3 = x3 + 3

# print table of seven in reverse:
x4 = 70
while(x4 >= 7):
    print(x4)
    x4 = x4 - 7

# while loop by using break statement

x5 = 5
while(x5 <= 15):
    if x5 == 9:
        break
    print(x5)
    x5 = x5 + 1

# while loop by using continue statement:

x6 = 6
while(x6 <= 15):
    if x6 == 11:
        x6 = x6 + 1
        continue
    print(x6)
    x6 = x6 + 1


x7 = 1
while(x7 <= 10):
    print(x7)
    x7 = x7 + 1