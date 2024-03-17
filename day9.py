# Dictionary:
#data is stored in specific manner like property value pair
info = {
    "key": "value",
    "property": "value",
    "firstname" : "Pooja",
    "lastname" : "Rahane"
}
print(info)

Vehicle = {
    "name" : "audi",
    "color": "white",
    "regNo": 1234,
    "city" : "mumbai",
    "regNo": 5555
}
print(Vehicle)

# retrive:
print(Vehicle["name"])
print(Vehicle["regNo"])

# Update:
Vehicle["color"] = "blue"
print(Vehicle)

# Add:
Vehicle["DOP"] = "21-Feb-024"
print(Vehicle)

# Delete:
del Vehicle["color"]
print(Vehicle)

# Vehicle.pop("DOP")
# print(Vehicle)

# del Vehicle: delete all the data
print(type(Vehicle))

# len: gives total no.of key-value-pair
print(len(Vehicle))

# In: gives boolean value-if element is present gives True otherwise false
print("regNo" in Vehicle)

# duplicate: does not consider duplicate ,consider as a updated
print(Vehicle)




