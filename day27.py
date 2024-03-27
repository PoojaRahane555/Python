# Polymorphism:
# 1)Overloading: Which is not possible in Python
# same class, same method name , different signature

class Calculator:

    def addition(self,a,b):
        print(a+b)
    
    def addition(self,a,b,c):
        print(a+b+c)
    
    def addition(self,a,b,c,d):
        print(a+b+c+d)

alpha = Calculator()
# alpha.addition(11,22)
# alpha.addition(11,22,33)
alpha.addition(11,22,33,44)

class Calculator2:

    def addition(self,l = None, m = None, n = None, o = None):

        if(l != None and m != None and n != None and o != None):
            print(l + m + n + o)
        elif(l != None and m != None and n != None):
            print(l + m + n)
        elif(l != None and m != None):
            print(l + m)

alpha2 = Calculator2()
alpha2.addition(10,20)
alpha2.addition(10,20,30)
alpha2.addition(10,20,30,40)




    
