# list:
# list stores value by index
# len(listName) gives total no.of items in given list
# len(listName) - 1 gives last index no.

#             0           1           2            3
village = ["Nandgaon","Chandgaon","Aapegaon","Shirasgaon"]
print(village)

# list stores value by index
print(village[2])

# update the element at specific index in the list
village[2] = "Ukkadgaon"

# no.of elements in list
print(len(village))

# last index no.
print(len(village) - 1)      


# loops on list:
# for loop 
# for loop with range
# while loop

# 1)for loop:
vegetables = ["brinjal","capsicum","chilli","cauliflower","beans","pumpkin"]

for x in vegetables:
    print(x)


# 2)for loop with range:

for x in range(len(vegetables)):
    # print(x)
    print(vegetables[x])

# forward loop
for x in range(6):
    print(x)
    print(vegetables[x])

# reverse loop
for x in range(len(vegetables)-1,-1,-1):
    print(x)
    print(vegetables[x])


# 3)while loop with list:
color = ["baby pink","sky blue","marron","baby blue","mint","peach"]
x1 = 0
while(x1 < len(color)):
    # print(x1)
    print(color[x1])
    x1 = x1 + 1

x2 = 0
while(x2 < 6):
    print(color[x2])
    x2 = x2 + 1

x3 = len(color)-1
while(x3 > -1):
    # print(x3)
    print(color[x3])
    x3 = x3 - 1
