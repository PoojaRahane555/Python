# dictionary:

info = {
    "firstname": "Pooja",
    "lastname" : "Lokhande",
    "age" : 25,
    "city" : "Mumbai"
}
print(info)
print(type(info))
print(len(info))

# retrive:
print(info['age'])

# update:
info["city"] = "Panvel"
print(info)

# add:
info["rollno"] = 1
print(info)

del info["rollno"]
print(info)

# in
print("city" in info)

# program 2:

vehicle = {
    "color" : "red",
    "regNo" : 1234
}
print(vehicle)
print(type(vehicle))
print(len(vehicle))

# vehicle.clear()
# print(vehicle)

# del vehicle
# print(vehicle)

# a = vehicle.popitem()
# print(a)
# vehicle.pop('color')
# print(vehicle)

# program 3:

animal = {
    "name" : "dog",
    "leg"  : 4,
    "color": "white"    
}
print(animal)
print(animal.update({"color":"black"}))
print(animal)

# loops on dictionary:
info3 = {
    "first_name" : "Pooja",
    "last_name" : "Lokhande",
    "age" : 26,
    "city" : "Panvel"
}

for x in info3:
    # print(x)
    # print(info3[x])
    print(x, info3[x])

for key in info3.keys():
    print(key)

for val in info3.values():
    print(val)

for k,v in info3.items():
    print(k,v)


