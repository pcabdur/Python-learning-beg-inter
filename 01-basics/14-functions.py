def greet(name):
    print(f"wasssup {name}")

greet("abddur")
greet("asm")

def introduce(name, age):
    print(f"My name is {name}")
    print(f"I am {age} years old")
introduce("pcas",19)


def add(a, b):
    print(a + b)

add(222,1211)

# this returst and exit bruh i mean we can sue this to reture that vales to  the para meter of the functioin  bruh 


def add(a, b):
    return a + b

result=add(22,32)
print(result)


def calculate(a, b):
    addition = a + b
    subtraction = a - b

    return addition, subtraction


x, y = calculate(20, 5)

print(x)
print(y)


##3 default para meter btuh 


def greet(name="Abdur"):
    print(f"Hello {name}")


greet()


def introduce(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")

introduce("Abdur", 20)


def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"


print(check_age(20))
print(check_age(15))


'''

Outside function
      │
      │
      ├── function
      │      ↓
      │   message
      │
      │
      └── cannot directly access message



'''
name = "Abdur"


def greet():
    print(name)


greet()


## functin calling another fucntion bruh 


def add(a, b):
    return a + b


def double(number):
    return number * 2


result = add(10, 20)
answer = double(result)

print(answer)



def greed(name):
    print(f"hello {name}")

greed("abdur")

def o_or_evn(num):
    if(num%2==0):
        return(True)
    else:
        return(False)
print(o_or_evn(32))


def celsius_to_fahrenheit(celsius):

    F = (celsius * 9/5) + 32
    return F
print("far",celsius_to_fahrenheit(int(input())))


def calculate_average():

    ##map is used to taransforsm a list  based on a function 
    marks=list(map(int,input().split(","," ")))
    print(marks)
calculate_average()


