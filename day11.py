info = {
    "firstName" : "Aarvi",
    "lastName"  : "Lokhande",
    "age" : 3,
    "city" : "Panvel"
}
print(info)
print(len(info))
print(type(info))

print(info["firstName"])
print(info.get('firstName'))

aa = info.setdefault("rollNo",12)
print(aa)
print(info)

# info2 = dict.fromkeys("keyone","keytwo")
# print(info2)
info2 = dict.fromkeys(["keyone","keytwo","keythree"])
print(info2)


students = [
    {
        "firstName":"Pooja",
        "lastName":"Lokhande",
        "age":25,
        "skills":["html","css","js"]
    },
    {
        "firstName":"Kavita",
        "lastName":"Rahane",
        "age":19,
        "skills":["html","css","js","python"]
    },
    {
        "firstName":"Babita",
        "lastName":"Jagtap",
        "age":34,
        "skills":["html","css","js"]

    }
]
print(students)
print(len(students))
print(type(students))
print(type(students[1]))

# print firstname of third element
print(students[2]["firstName"])
print("..........................")

# print all the firstName:
for x in students:
    print(x["firstName"])

# print user with python skills:
for x in students:
    if 'python' in x['skills'] :
        print(x["firstName"])

print("////////////////////////////////////////")

# print user with python skills and age greater than 25:
for x in students:
    if x["age"] > 15 and 'python' in x["skills"]:
        print(x["firstName"],x["age"],x["skills"])

# print name and no.of skills:
for x in students:
    print(x["firstName"]  +" :"+ str(len(x["skills"])))

# print average age of all the students:
total = 0
for x in students:
    total = total + x["age"]
print(total/len(students))


    

    