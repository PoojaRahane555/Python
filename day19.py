# lambda function:
def sub(x,y):
    return x-y
aa = sub(10,5)
print(aa)

add = lambda x,y : x+y
bb = add(11,11)
print(bb)

square = lambda x : x*x
cc = square(5)
print(cc)

# function as parameter to another function:
divide = lambda x,y : x/y

def div(fn,x,y):
    d = fn(x,y)
    return d
dd = div(divide,40,8)
print(dd)

sub = lambda x,y : x - y

def substraction(fn,x,y):
    e = fn(x,y)
    return e
ee = substraction(sub,22,6)
print(ee)

# function as return type
add = lambda x,y : x+y

def addition():
    return lambda x,y : x+y
ff = addition()
print(ff)

f = ff(56,65)
print(f)