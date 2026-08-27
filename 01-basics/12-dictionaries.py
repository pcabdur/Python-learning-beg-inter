user = {
    "name": "Abdur",
    "age": 20,
    "language": "Python"
}

print(user)
print(type(user))

users = {
    "name": "Abdur",
    "age": 20
}
#change chares burh 
users["country"] = "India"

print(users)

user.pop("age")

del user["country"]
user.clear()

print(len(users))

print(users.keys())

for va in users.values():
    print(va)


for key, value in users.items():
    print(key, value)

# so we dont what what is indse so 
# so we can go if we dont knw    so we use get()

print(users.get("email"))
user = {
    "name": "Abdur",
    "age": 20,
    "address": {
        "city": "Chennai",
        "country": "India"
    }
}
print(user["address"])
print(user["address"]["city"])

users = [
    {"name": "Abdur", "age": 20},
    {"name": "Ali", "age": 21},
    {"name": "Ahmed", "age": 22}
]

print(users[0]["name"])


for user in users:
    print(user["name"])

'''Abdur
Ali
Ahmed'''


students = [
    {"name": "Abdur", "age": 20, "mark": 90},
    {"name": "Ali", "age": 21, "mark": 85},
    {"name": "Ahmed", "age": 19, "mark": 95}
]

# Print each student
for student in students:
    print(
        f"Name: {student['name']} | "
        f"Age: {student['age']} | "
        f"Mark: {student['mark']}"
    )

# Find highest mark
highest_mark = 0

for student in students:
    if student["mark"] > highest_mark:
        highest_mark = student["mark"]

print("Highest mark:", highest_mark)

response = {
    "status": "success",
    "data": {
        "user": {
            "name": "Abdur",
            "skills": ["Python", "Docker", "AWS"]
        }
    }
}

print(response["status"])
print(response["data"]["user"]["name"])
print(response["data"]["user"]["skills"][0])
