# string:
# 1)UPPER: convert all the characters into upper case
ffirst_name = "Tukaram"
print(ffirst_name)
print(type(ffirst_name))
print(len(ffirst_name))

aa = ffirst_name.upper()
print(aa)

# 2)LOWER: convert all the character into lowercase
last_name = "RAHANE"
print(last_name)

bb = last_name.lower()
print(bb)

# 3)ISUPPER : returns boolean value
middle_name = "RAGHUNATHA"
print(middle_name)

cc = middle_name.isupper()
print(cc)

# 4)ISLOWER: returns boolean value
first_name = "aarvi"
print(first_name)

dd = first_name.islower()
print(dd)

# 5)STARTSWITH: returns boolean value
vehicle = "sedane"
print(vehicle)
ee = vehicle.startswith('se')
print(ee)

# 6)ENDSWITH: returns boolean value
ff = vehicle.endswith('E')
print(ff)

# 7)COUNT: count the  given character
gg = vehicle.count('e')
print(gg)

# 8)LSSTRIP: removes the starting space 
furniture = "  Cupboard"
print(furniture)
print(len(furniture))

hh = furniture.lstrip()
print(hh)

# 9)RSSTRIP: removes the ending space
furniture2 = "Table..   "
print(furniture2)
print(len(furniture2))

ii = furniture2.rstrip()
print(ii)

# 10)STRIP: removes the starting as well ending space
furniture3 = "   Chair   "
print(furniture3)
print(len(furniture3))

jj = furniture3.strip()
print(jj)

# 11)Replace: 
info = "I am learning python"
print(info)

kk = info.replace('python',"javascript")
print(kk)

# 12)ISDIGIT: returns boolean value =>>  0 - 9 (only true for integer,special character-false)
ll = '11.1'.isdigit()
print(ll)

mm = '123'.isdigit()
print(mm)

mmm = "1%".isdigit()
print(mmm)


# 13)ISALPHA: returns boolean value  ==>>(only true for alphabates ,special charactes-false)
nn = '555$'.isalpha()
print(nn)

oo = "abcd".isalpha()
print(oo)

pp = "abcd@".isalpha()
print(pp)

# 14)ISALNUM:  returns boolean value ==>true-integer, float-false, true-alpha, true:alpha-integer,false-spl.char.
qq = '6066'.isalnum()
print(qq)

rr = "hello".isalnum()
print(rr)

ss = "pooja123".isalnum()
print(ss)

tt = "aaa12%".isalnum()
print(tt)

print('................................................')
# 15)ISSPACE: returns boolean value  ==>true-only for blank space, false-space with character,number
product = " herbal"
qqq = product.isspace()
print(qqq)

product2 = " "
rrr = product2.isspace()
print(rrr)

product3 = " 56 "
sss = product3.isspace()
print(sss)

# 16)Capitalize: convert first character into capitalcase rest lower case
flower = "lotus"
ttt = flower.capitalize()
print(ttt)

goodT = "be the best version of yourself"
uuu = goodT.capitalize()
print(uuu)

# 17)ISTITLE: returns boolean value   ==>only true for all first char. must in capitalcase,rest false
info = "I am learning testing tools"
print(info)

vvv = info.istitle()
print(vvv)

info2 = "Best Version Of Yourself" 
print(info2)
www = info2.istitle()
print(www)

# 18)SPLIT: split string at given char. and returns list
email = "poojalokhande63836@gmail.com"
print(email)
xxx = email.split('@')
print(xxx)

# 19)JOIN: join element by given character and returns string
basket = ["pen","book","bottle","12"]
print(basket)

yyy = ('--').join(basket)
print(yyy)

# 20)FIND:
emailId = "poojalokhande63@gmail.com"
zz = emailId.find('o')
print(zz)

zzz = emailId.find('a',5)
print(zzz)

# 21)REMOVEPREFIX:
city2 = "Amravati"
a1 = city2.removeprefix('Am')
print(a1)

# 22)REMOVESUFFIX:
id =  "kanchanrahane18@gmail.com"
id2 = "poojarahane63836@gmail.com"
id3 = "aarvilokhande55@gmail.com"

emails = [id, id2, id3]
print(emails)

names = []

for x in emails:
    a2 = x.removesuffix('@gmail.com')
    names.append(a2)
print(names)   

# 
students = {
    "1" : "PoojaAdmin",
    "2" : "KavitaCEO",
    "3" : "KanchanCustomer",
    "4" : "AarviManager"

}
# print(students)

role = ["Admin","CEO","Customer","Manager"]
employee = []

for key in students.values():
    for x in role:
        if x in key:
            a3 = key.removesuffix(x)
            employee.append(a3)
print(employee)

# 23)SWAPCASE: convert small character into uppercase and capital letter into small case
toy = "remoteCar"
print(toy.swapcase())

# ZFILL: adds zero for remaining index
college = "V.Patil"
print(college)
aaa = college.zfill(10)
print(aaa)







