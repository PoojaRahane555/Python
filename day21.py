# program 1: print age according to their years 
years = [1998,1999,2000,2001,2002]

# a)by for loop:
age = []
for x in years:
    age.append(2024-x)
print(age)

# b)by map method:
aa = list(map(lambda x: 2024-x,years))
print(aa)

# c)by list comprehension :
aaa = [2024-x for x in years]
print(aaa)

# program 2:
names = ["Sanvi","Kanvi","Avantika","Ketaki","Sayali"]

# a)by for loop:
name = []
for x in names:
    if len(x) > 5:
        name.append(x)
print(name)

# b) by filter method:
bb = list(filter(lambda x : len(x) > 5,names))
print(bb)

# c) by list comprehension:
bbb = [x for x in names if len(x) > 5]
print(bbb)

# program 3: Print deposit and withdral
history = [-106,5000,-850,-399,9999,-2100,1200,-2000]

# a)by for loop:
transacation = []
for x in history:
    if x > 0:
        transacation.append("deposit")
    else:
        transacation.append("withdral")
print(transacation)

# b)by filter method:
cc1 = list(filter(lambda x : x > 0, history))
print(cc1)

cc2 = list(filter(lambda x : x < 0, history))
print(cc2)

# c)by list comprehension:
ccc = ["deposit" if x > 0 else "withdral" for x in history]
print(ccc)

