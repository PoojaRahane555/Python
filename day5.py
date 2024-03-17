# print one to seven:
for x in range(1,8):
    print(x)

# print seven to one in reverse:
for x in range(7,0,-1):
    print(x)


# print table of 9:
for x in range(9,91,9):
    print(x)

# print table of eight:
for x in range(1,11):
    print(x*8)


# print table of eleven in reverse:
for x in range(110,10,-11):
    print(x)

# print table of thirteen in reverse:
for x in range(10,0,-1):
    print(x * 13)


# for loop by using break statement:
for x in range(1,7):
    if x == 5:
        break
    print(x)

for x in range(10,1,-2):
    print(x)
    if x == 4:
        break


# for loop by using continue statement:
for x in range(1,7):
    if x == 4:
        continue
    print(x)

for x in range(30,2,-3):
    if x == 18:
        continue
    print(x)