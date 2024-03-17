# conditional statement:
# used for one input and multiple output
# program 1
numT = 9
if numT > 0 and numT <=5 :
    print("10 % discount")
if numT > 5 and numT <=10:
    print("20 % discount")  
if numT > 10 and numT <=20:
    print("30 % discount")

# program 2
numT = -1
if numT > 0 and numT <=5 :
    print("10 % discount")
elif numT > 5 and numT <=10:
    print("20 % discount")  
elif numT > 10 and numT <=20:
    print("30 % discount")
else:
    print("Incorrect Input")

# program 3
    
marks = 67

if marks > 90:
    print("passed with grade A")
if marks > 70:
    print("passed with grade B")
if marks > 50:
    print("passed with grade C")


# program 4
    
marks = 89

if marks > 90:
    print("grade A")
elif marks > 70:
    print("grade B")
elif marks > 50:
    print("grade C")
else:
    print("try again...")


# program 5

x = 10
y = 5

if x > y:
    print("x is grater")
else:
    print("y is greater")


# program 6:
a = 1
b = 2 
c = 3

if a > b and a > c:
    print("a is greater")
elif b > a and b > c:
    print("b is grater")
elif c > a and c > b:
    print("c is greater")
else:
    print("incorrect input")