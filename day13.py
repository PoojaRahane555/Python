# for loop:

# program 1
city = "Gondiya"
for x in city:
    print(x)

# program 2:
for x in range(len(city)):
    print(city[x])

# print using reverse loop:
for x in range(len(city)-1,-1,-1):
    print(city[x])


# program 3:
name = "Arvind"
for x in range(6):
    # print(x)
    print(name[x])

# reverse loop:
for x in range(5,-1,-1):
    # print(x)
    print(name[x])

print("in" in name)


# While-loop:
color = "baby-pink"
i = 0
while(i < len(color)):
    # print(i)
    print(color[i])
    i = i + 1

# reverse loop:
i2 = len(color)-1
while(i2 >= 0):
    print(color[i2])
    i2 = i2 - 1
