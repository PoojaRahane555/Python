# program 1:
import pickle


with open('info4.txt','w') as f:
    f.write("Hello Everyone...")
    f.write("I am learning python.")

# program 2:

with open('info4.txt','r') as f1:
    str = f1.read()
    print(str)

# program 3:
class Employee:
    def __init__(self,fn,ln,eml,ag):
        self.firstName = fn
        self.lastName = ln
        self.email = eml
        self.age = ag

    def displayInfo(self):
        print(self.firstName)
        print(self.lastName)
        print(self.email)
        print(self.age)

f = open('student.dat','wb')
n = int(input('Enter the no. of objects'))

for x in range(n):
    fn = input("Enter firstName")
    ln = input("Enter lastName")
    eml = input('Enter email')
    ag = input('Enter age')
    e = Employee(fn,ln,eml,ag)
    pickle.dump(e,f)
    
f.close()   
# python object ===> data file write
# data read  ==> python object  ==> displayInfo()