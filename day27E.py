# Program 1:

class Bank:
    country = "India"
    count = 0

    def __init__(self,fn,ln,acc,blc):
        self.firstName = fn
        self.lastName = ln
        self.account = acc
        self.balance = blc
        self.transaction = []
        Bank.count = Bank.count + 1

    def deposit(self,amount):
        self.balance = self.balance + amount
        self.transaction.append(amount)

    def withdrawl(self,amount):
        if  self.balance > amount:
            self.balance = self.balance - amount
            self.transaction.append(-amount)
        else:
            print("Insufficient amount")
        
    def lastFiveTransc(self,x):
        return self.transaction[-x::]

    @classmethod
    def updateCountry(cls,cnty):
        cls.country = cnty

    @staticmethod
    def objectCount():
        return Bank.count

pooja = Bank("Pooja","Rahane",123,100000)
kanchan = Bank("Kanchan","Khilari",565,90000)
kanvi = Bank("Kanvi","Lokhande",6565,80000)
dipak = Bank("Dipak","Lokhande",555,70000)
sagar = Bank("Sagar","Khilari",666,60000)

print(pooja.firstName)
print(pooja.lastName)
print(pooja.balance)
print(pooja.account)
print(pooja.country)
print(pooja.count)

print(Bank.objectCount())
pooja.country = "Bharat"
print(pooja.country)
print(kanchan.country)

pooja.deposit(20000)
pooja.deposit(25000)
pooja.withdrawl(70000)
pooja.deposit(5000)
pooja.withdrawl(2999)

aa = pooja.lastFiveTransc(5)
print(aa)

