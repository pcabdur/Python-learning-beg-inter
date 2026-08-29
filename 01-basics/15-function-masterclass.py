def add(*num):
    print(num)
add(10,20,30,40)

def total(*numbers):
    result = 0

    for number in numbers:
        result += number

    return result
print(total(10, 20))
print(total(10, 20, 30))
print(total(1, 2, 3, 4, 5))

def profile(**details):

    for key, value in details.items():
        print(key, ":", value)



profile(
    name="Abdur",
    age=20,
    country="India"
)

def std(name,*skill,**details):
    print("name:",name)

    print("skills:")
    for skills in skill:
        print("-",skills)
    print("Detail:")
    for key,val in details.items():
        print(key,":",val)
std(
    "Abdur",
    "Python",
    "Docker",
    "AWS",
    age=20,
    country="India"
)

# ==========================================
# LESSON 15 - FUNCTION MASTERCLASS
# ==========================================


# 1. POSITIONAL ARGUMENTS

def introduce(name, age):
    print("Name:", name)
    print("Age:", age)


introduce("Abdur", 20)


# 2. KEYWORD ARGUMENTS

introduce(age=20, name="Abdur")


# 3. DEFAULT ARGUMENT

def greet(name="Abdur"):
    print(f"Hello {name}")


greet()
greet("Ali")


# 4. *args

def total(*numbers):
    result = 0

    for number in numbers:
        result += number

    return result


print(total(10, 20))
print(total(10, 20, 30))
print(total(1, 2, 3, 4, 5))


# 5. **kwargs

def show_profile(**details):

    for key, value in details.items():
        print(key, ":", value)


show_profile(
    name="Abdur",
    age=20,
    country="India"
)


# 6. *args + **kwargs

def student(name, *skills, **details):

    print("Name:", name)

    print("Skills:")

    for skill in skills:
        print("-", skill)

    print("Details:")

    for key, value in details.items():
        print(key, ":", value)


student(
    "Abdur",
    "Python",
    "Docker",
    "AWS",
    age=20,
    country="India"
)


# 7. LIST UNPACKING

numbers = [10, 20, 30]


def add(a, b, c):
    return a + b + c


print(add(*numbers))


# 8. DICTIONARY UNPACKING

user = {
    "name": "Abdur",
    "age": 20
}


def display_user(name, age):
    print("Name:", name)
    print("Age:", age)


display_user(**user)


# 9. KEYWORD-ONLY ARGUMENTS

def create_user(name, *, age, country):
    print(name, age, country)


create_user(
    "Abdur",
    age=20,
    country="India"
)

def student_profile(name, *skills, **details):
    print(name)


    print("skills:")
    for i in skills:
        print("-",i)
    print("Details:")
    for i,j in details.items():
        print(i ,":",j)

student_profile(
    "Abdur",
    "Python",
    "AWS",
    "Docker",
    "Git",
    age=20,
    country="India",
    goal="Python Master"
)