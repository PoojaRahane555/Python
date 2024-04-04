# Exception Handling
# Built In, User define, custom raising error/exception

# program 1: Zero division error - division by zero
x = 12
y = 3
z = 0

# print(x*y)
# print(x/z) #this is an exception
# print('Hello World..')

# handling
a = 10


try:
    b = 0
    c = a/b
    print(c)
except:
    print('some error occured')

print('Hello World...')

# program 2: Syntax error - this has to be changed maually
# print('Welcome)            #unterminated string literal
print('Welcome')

# program 3: Index error - string index out of range
name = "Kanvi"
print(name)
print(name[0])
# print(name[6]) #this is an exception 

# handling
try:
    print(name[6])
except:
    print('error-occured')

print('Welcome Princess')

# program 4: Type error - unsupported operand type(s) for +: 'int' and 'str'
l = 12
m = "twelve"
# n = l + m   #this is an exception
# print(n)

try:
    print(l + m)
except:
    print("something went wrong")

# program 5: providing more specific Error type using basic exception class
a1 = 11
try:
    b1 = 11
    city = "Panvel"
    c1 = a1/b1
    print(c1)
    print(city[6])
except Exception as e:
    print("Some error occured....",e)
print("bye bye")

a2 = 10
animal = "Dog"
try:
    b2 = 0
    c2 = a2/b2
    print(animal[1])
except Exception as f:
    print("error is...",f)

# program6: using multiple except blocks for specific errors
# for the developer team
a3 = 50
color = "baby-pink"
try:
    b3 = 5
    c3 = a3/b3
    print(color[9])
except Exception as g:
    print('Error is...',g)
except Exception-2 as h:
    print('Error is...',h)

a4 = 14
dress = "T-Shirt"
try:
    b4 = 0
    c4 = a4/b4
    print(c4)
    print(dress[2])
except ZeroDivisionError as i:
    print('Error occured:',i)
except IndexError as j:
    print('Error occured:',j)

# Program 7: by using else
# else block executed only when there is no exception
num1 = 20
names = "Prashant"
try:
    num2 = 4
    num3 = num1/num2
    print(num3)
    print(names[4])
except Exception-3 as k:
    print('Some error occured-',k)
except Exception-4 as l:
    print('Some error occured-',l)
else:
    print("Code Executed successfully..")

print("Nice to meet you")

# Program 8: by using finally
# irrespecive try or expect block it will execute always
add1 = 15
Gender = "Female"
try:
    add2 = 15
    add3 = add1 + add2
    print(add3)
    print(Gender[3])
except Exception-5 as m:
    print("The error is as:",m)
except Exception-6 as n:
    print("The error is as:",n)
else:
    print("Code Executed Successfully....")
finally:
    print("I will always execute")

div1 = 15
Gender = "Male"
try:
    div2 = 0
    div3 = div1/div2
    print(div3)
    print(Gender[5])
except Exception as o:
    print("The error is as:",o)
except Exception-8 as p:
    print("The error is as:",p)
else:
    print("Code Executed Successfully....")
finally:
    print("I will always execute")
















    