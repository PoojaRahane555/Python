# type
x = 5
print(x)
print(type(x))

y = 0.6
print(y)
print(type(y))

z= [1,2,3]
print(z)
print(type(z))

info = {
    "first_name" : "Pooja",
    "last_name"  : "Lokhande"
}
print(info)
print(type(info))

name = "Kanvi"
print(name)
print(type(name))

# String:
city = 'Panvel'
print(city)

flower = "Lotus"
print(flower)

bird = '''Parrot'''
print(bird)

detail = """I am learning python."""
print(detail)

# program 1:
color = "Lavendar"
print(color[0])
print(color[1])
print(color[5])
# print(color[9])   =>string index out of range
print(len(color))

# Methods:
# 1)Upper: convert all the character into uppercase
name = "aarvi"
aa = name.upper()
print(aa)

# 2)Lower: convert all the character into smallcase
vegetable = "GinGer"
bb = vegetable.lower()
print(bb)

# 3)Count: count the repetative element
num = '12123123412345'
print(num)
cc = num.count('2')
print(cc)

fruit = "banana"
dd = fruit.count('a')
print(dd)

# 4)Slice:
name2 = "Chandrakant"

        # 0    1    2    3    4    5    6    7    8    9    10
# name2 = C    h    a    n    d    r    a    k    a    n    t
        #-11  -10  -9   -8   -7   -6   -5   -4   -3   -2    -1

# print(starting index: End index(excluded) : step size)
print(name2)
print(name2[5::])
print(name2[0::])
print(name2[-3:]) 
print(name2[5:-2])
print(name2[-10:-3])
# print(name2[-2:-6])  returns blank string
print(name2[2:8:1])
print(name2[0:11:2])
print(name2[0:11:3])
print(name2[0:11:4])

