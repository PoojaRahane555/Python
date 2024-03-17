# VARIABLES

m = 5
print(m)
m = 6
print(m)

n = 10
print(n)
n = 1
print(n)

sum = m + n
diff = m - n
print(sum)
print(diff)

# ARITHMATIC OPERATION(+ , - , * , / , %)
p = 55
q = 5
print(p + q)
print(p - q)
print(p * q)
print(p / q)
print(p % q)

r = 66
s = 6
print(r + s)
print(r - s)
print(r * s)
print(r / s)
print(r % s)

# FUNCTION:  to avoid repetation of the code function are used

def Calculator(x,y):
    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)
    print(x % y)

Calculator(20,4)
Calculator(100,3)
Calculator(22,2)

# function without parameter and without return type:
def addA():
    print(55 + 55)
addA()
addA()
addA() 


# function with parameter and without return type:
def addB(a,b):
    print(a + b)
addB(20,10)
addB(6,5)
addB(9,7)


# function with parameter and with return type:
def addC(c,d):
    return c + d
e = addC(35,9)
print(e)
print(e + e)
print(e * e)

