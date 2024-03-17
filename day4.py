# loops:
# used for to avoid repetation of the code
# 1)for loop : 
# for x in range(starting index,ending index-excluded,stepsize):
    # print(x)   -statements

for x in range(5):
    print(x)

# if starting index is not given then consider zero as default

# print one to five:
for x in range(1,6):
    print(x)

# print reverse ten to one:
for x in range(10,0,-1):
    print(x)

# print table of two:
for x in range(2,21,2):
    print(x)


# print table of 15:
for x in range(15,151,15):
    print(x)

# print table of five in reverse:
for x in range(50,4,-5):
    print(x)


# for loop by using break:
for x in range(1,7):
    if x == 4:
        break
    print(x)

for x in range(10,0,-1):
    print(x)
    if x == 5:
        break