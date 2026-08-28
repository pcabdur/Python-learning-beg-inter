# Python From Scratch --- Lessons 01--14 Quick Reference

This README is a compact revision sheet for everything learned so far.

Use it as a quick reference while practicing. The goal is not to
memorize everything immediately, but to understand when and why each
feature is used.

------------------------------------------------------------------------

# Lesson 01 --- Hello Python

## `print()`

Displays something on the screen.

``` python
print("Hello Python")
```

Output:

``` text
Hello Python
```

## `\t`

Adds a tab.

``` python
print("\tProfile")
```

## Basic string output

``` python
print("================")
print("Name: Abdur")
print("================")
```

------------------------------------------------------------------------

# Lesson 02 --- Variables

Variables store references to values.

``` python
name = "Abdur"
age = 20
height = 185
is_student = True
```

## `print()`

``` python
print(name)
```

## Reassigning a variable

``` python
age = 20
age = 22
```

The variable now refers to `22`.

## Arithmetic with variables

``` python
x = 10
y = 20

print(x + y)
```

## String concatenation

``` python
x = "10"
y = "20"

print(x + y)
```

Output:

``` text
1020
```

Because both values are strings.

## Assignment operators

``` python
age += 5
```

Same idea as:

``` python
age = age + 5
```

Other examples:

``` python
x -= 2
x *= 3
x /= 2
```

------------------------------------------------------------------------

# Lesson 03 --- Data Types

## String --- `str`

Text.

``` python
name = "Abdur"
print(type(name))
```

## Integer --- `int`

Whole numbers.

``` python
age = 20
print(type(age))
```

## Float --- `float`

Decimal numbers.

``` python
price = 99.55
print(type(price))
```

## Boolean --- `bool`

`True` or `False`.

``` python
is_python_fun = True
is_python_hard = False
```

## None --- `NoneType`

Represents the absence of a value.

``` python
result = None
print(type(result))
```

## `type()`

Checks the type of a value.

``` python
print(type(20))
print(type("hello"))
print(type(True))
```

------------------------------------------------------------------------

# Lesson 04 --- Operators

## Arithmetic operators

``` python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
```

### Important

`/` → normal division

`//` → floor division

`%` → remainder

`**` → power

## Comparison operators

These return `True` or `False`.

``` python
print(10 > 5)
print(10 < 5)
print(10 == 10)
print(10 != 5)
print(10 >= 10)
print(10 <= 10)
```

## Logical operators

### `and`

Both conditions must be true.

``` python
age = 20

print(age >= 18 and age <= 30)
```

### `or`

At least one condition must be true.

``` python
print(age < 18 or age > 60)
```

### `not`

Reverses a boolean.

``` python
is_student = True

print(not is_student)
```

------------------------------------------------------------------------

# Lesson 05 --- Input

## `input()`

Gets text from the user.

``` python
name = input("Enter your name: ")

print(name)
```

Important:

`input()` returns a **string**.

Even if the user enters:

``` text
20
```

Python initially receives:

``` python
"20"
```

------------------------------------------------------------------------

# Lesson 06 --- Type Conversion

Convert one data type into another.

## `int()`

``` python
age = int("20")

print(age)
print(type(age))
```

## `float()`

``` python
price = float("99.5")
```

## `str()`

``` python
age = 20

message = str(age)
```

## `bool()`

``` python
value = bool(1)

print(value)
```

A common pattern:

``` python
age = int(input("Enter age: "))
```

This means:

``` text
input()
   ↓
string
   ↓
int()
   ↓
integer
```

------------------------------------------------------------------------

# Lesson 07 --- Conditionals

## `if`

Runs code when a condition is true.

``` python
age = 20

if age >= 18:
    print("Adult")
```

## `else`

Runs when the `if` condition is false.

``` python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

## `elif`

Checks another condition.

``` python
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")
```

## `and`

``` python
if age >= 18 and age <= 60:
    print("Working age")
```

## `or`

``` python
if age < 18 or age > 60:
    print("Outside range")
```

## Nested conditions

``` python
if age >= 18:
    if age >= 21:
        print("21 or older")
```

------------------------------------------------------------------------

# Lesson 08 --- Loops

Loops repeat code.

## `for`

``` python
for i in range(5):
    print(i)
```

Output:

``` text
0
1
2
3
4
```

## `range()`

``` python
range(5)
```

means:

``` text
0 1 2 3 4
```

Other forms:

``` python
range(1, 6)
range(0, 10, 2)
```

## Loop through a string

``` python
for char in "Python":
    print(char)
```

## `while`

Repeats while a condition is true.

``` python
count = 1

while count <= 5:
    print(count)
    count += 1
```

## `break`

Stops the loop.

``` python
for i in range(10):
    if i == 5:
        break

    print(i)
```

## `continue`

Skips the current iteration.

``` python
for i in range(5):
    if i == 2:
        continue

    print(i)
```

------------------------------------------------------------------------

# Lesson 09 --- Lists

Lists store ordered collections.

``` python
names = ["Abdur", "Ali", "Ahmed"]
```

## Indexing

``` python
print(names[0])
```

## Negative indexing

``` python
print(names[-1])
```

## Change an element

Lists are mutable.

``` python
names[1] = "Rahul"
```

## `len()`

``` python
print(len(names))
```

## `append()`

Adds to the end.

``` python
names.append("Ahmed")
```

## `insert()`

Adds at a specific index.

``` python
names.insert(1, "PCA")
```

## `remove()`

Removes a value.

``` python
names.remove("Ali")
```

## `pop()`

Removes an item by index, or the last item if no index is supplied.

``` python
names.pop()
names.pop(1)
```

## `in`

Checks membership.

``` python
print("Abdur" in names)
```

## `sort()`

Sorts the list.

``` python
numbers = [30, 10, 20]
numbers.sort()

print(numbers)
```

## `reverse()`

Reverses the current order.

``` python
numbers.reverse()
```

## `count()`

Counts occurrences.

``` python
numbers = [10, 10, 20]

print(numbers.count(10))
```

## `index()`

Finds the index of a value.

``` python
names = ["Abdur", "Ali"]

print(names.index("Ali"))
```

## `enumerate()`

Gets index and value while looping.

``` python
names = ["Abdur", "Ali"]

for index, name in enumerate(names):
    print(index, name)
```

------------------------------------------------------------------------

# Lesson 10 --- Tuples

Tuples are ordered and immutable.

``` python
numbers = (10, 20, 30)
```

## Indexing

``` python
print(numbers[0])
```

## Slicing

``` python
print(numbers[1:3])
```

## `len()`

``` python
print(len(numbers))
```

## `count()`

``` python
numbers = (10, 10, 20)

print(numbers.count(10))
```

## `index()`

``` python
names = ("Abdur", "Ali")

print(names.index("Ali"))
```

## Tuple unpacking

``` python
person = ("Abdur", 20, "India")

name, age, country = person
```

Now:

``` python
print(name)
print(age)
print(country)
```

## Swapping values

Python allows:

``` python
x = 10
y = 20

x, y = y, x
```

Now:

``` text
x = 20
y = 10
```

------------------------------------------------------------------------

# Lesson 11 --- Sets

Sets store unique values.

``` python
numbers = {10, 20, 30}
```

## Duplicates disappear

``` python
numbers = {10, 20, 20, 30, 30}

print(numbers)
```

Result contains only:

``` text
10, 20, 30
```

## `add()`

``` python
names = {"Abdur", "Ali"}

names.add("Ahmed")
```

## `remove()`

``` python
names.remove("Ali")
```

Raises an error if the value doesn't exist.

## `discard()`

``` python
names.discard("Rahul")
```

Does not raise an error if the value is missing.

## `pop()`

Removes and returns an arbitrary set element.

``` python
item = names.pop()
```

## `in`

``` python
print("Abdur" in names)
```

## Union --- `|`

Combines sets.

``` python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
```

Result:

``` text
{1, 2, 3, 4, 5}
```

## Intersection --- `&`

Gets values shared by both.

``` python
print(a & b)
```

Result:

``` text
{3}
```

## Difference --- `-`

Values in the first set but not the second.

``` python
print(a - b)
```

Result:

``` text
{1, 2}
```

## Symmetric difference --- `^`

Values that are in either set but not both.

``` python
print(a ^ b)
```

Result:

``` text
{1, 2, 4, 5}
```

## Empty set

Important:

``` python
{}
```

is an empty dictionary.

Use:

``` python
set()
```

for an empty set.

------------------------------------------------------------------------

# Lesson 12 --- Dictionaries

Dictionaries store data as key-value pairs.

``` python
user = {
    "name": "Abdur",
    "age": 20,
    "country": "India"
}
```

## Access a value

``` python
print(user["name"])
```

## Change a value

``` python
user["age"] = 21
```

## Add a key

``` python
user["language"] = "Python"
```

## `pop()`

``` python
user.pop("age")
```

## `del`

``` python
del user["country"]
```

## `clear()`

``` python
user.clear()
```

## `len()`

``` python
print(len(user))
```

## `in`

Checks whether a key exists.

``` python
print("name" in user)
```

## `keys()`

``` python
print(user.keys())
```

## `values()`

``` python
print(user.values())
```

## `items()`

Gets key-value pairs.

``` python
for key, value in user.items():
    print(key, value)
```

## `get()`

Safely gets a value.

``` python
print(user.get("email"))
```

With a default:

``` python
print(user.get("email", "No email"))
```

## Nested dictionaries

``` python
user = {
    "name": "Abdur",
    "address": {
        "city": "Chennai",
        "country": "India"
    }
}
```

Access:

``` python
print(user["address"]["city"])
```

## Dictionary containing a list

``` python
user = {
    "name": "Abdur",
    "skills": ["Python", "Docker", "AWS"]
}
```

Access:

``` python
print(user["skills"][0])
```

## List of dictionaries

``` python
users = [
    {"name": "Abdur", "age": 20},
    {"name": "Ali", "age": 21}
]

for user in users:
    print(user["name"])
```

------------------------------------------------------------------------

# Lesson 13 --- Strings

Strings are sequences of characters.

``` python
name = "Abdur"
```

## Indexing

``` python
print(name[0])
```

## Negative indexing

``` python
print(name[-1])
```

## Slicing

``` python
print(name[0:3])
```

## Reverse

``` python
print(name[::-1])
```

## `len()`

``` python
print(len(name))
```

## `upper()`

``` python
print(name.upper())
```

## `lower()`

``` python
print(name.lower())
```

## `strip()`

Removes whitespace from the beginning and end.

``` python
name = "  Abdur  "

print(name.strip())
```

## `replace()`

``` python
message = "I love Java"

print(message.replace("Java", "Python"))
```

## `find()`

Returns the index of a substring.

``` python
text = "Hello Python"

print(text.find("Python"))
```

Returns `-1` when not found.

## `count()`

``` python
text = "python python"

print(text.count("python"))
```

## `startswith()`

``` python
url = "https://example.com"

print(url.startswith("https"))
```

## `endswith()`

``` python
filename = "model.py"

print(filename.endswith(".py"))
```

## `in`

``` python
text = "I am learning Python"

print("Python" in text)
```

## `split()`

Converts a string into a list.

``` python
sentence = "I love Python"

words = sentence.split()

print(words)
```

Result:

``` python
["I", "love", "Python"]
```

Using a separator:

``` python
data = "Abdur,20,India"

print(data.split(","))
```

## `join()`

Converts a list into a string.

``` python
words = ["I", "love", "Python"]

sentence = " ".join(words)

print(sentence)
```

## F-strings

Insert variables/expressions into strings.

``` python
name = "Abdur"
age = 20

print(f"My name is {name} and I am {age}.")
```

Expressions also work:

``` python
x = 10
y = 20

print(f"Sum: {x + y}")
```

## String immutability

You cannot change an individual character:

``` python
name = "Abdur"

# This causes an error:
# name[0] = "X"
```

Instead, create a new string.

------------------------------------------------------------------------

# Lesson 14 --- Functions

Functions are reusable blocks of code.

## `def`

Defines a function.

``` python
def greet():
    print("Hello bruh")
```

## Calling a function

``` python
greet()
```

## Parameter

``` python
def greet(name):
    print(f"Hello {name}")
```

`name` is the parameter.

## Argument

``` python
greet("Abdur")
```

`"Abdur"` is the argument.

## Multiple parameters

``` python
def introduce(name, age):
    print(name)
    print(age)

introduce("Abdur", 20)
```

## `return`

Sends a value back.

``` python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

## `print()` vs `return`

`print()` displays a value.

`return` gives a value back to the caller.

Example:

``` python
def square(number):
    return number * number

result = square(5)
```

Now `result` contains `25`.

## Multiple return values

``` python
def calculate(a, b):
    return a + b, a - b

addition, subtraction = calculate(20, 5)
```

## Default parameter

``` python
def greet(name="Abdur"):
    print(f"Hello {name}")

greet()
```

## Keyword arguments

``` python
def introduce(name, age):
    print(name, age)

introduce(age=20, name="Abdur")
```

## Conditions inside functions

``` python
def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"
```

## Loops inside functions

``` python
def print_numbers():
    for i in range(1, 6):
        print(i)
```

## Local variable

``` python
def greet():
    message = "Hello"
    print(message)
```

`message` belongs to the function's local scope.

## Function calling another function

``` python
def add(a, b):
    return a + b

def double(number):
    return number * 2

result = add(10, 20)
answer = double(result)

print(answer)
```

------------------------------------------------------------------------

# 🧠 Collection Cheat Sheet

## List

``` python
items = [1, 2, 3]
```

Use when:

> Order matters and the data may change.

------------------------------------------------------------------------

## Tuple

``` python
items = (1, 2, 3)
```

Use when:

> You want an ordered collection that should not be modified.

------------------------------------------------------------------------

## Set

``` python
items = {1, 2, 3}
```

Use when:

> You care about unique values and membership.

------------------------------------------------------------------------

## Dictionary

``` python
items = {
    "name": "Abdur",
    "age": 20
}
```

Use when:

> You want to associate keys with values.

------------------------------------------------------------------------

# 🔑 Most Important Python Keywords/Functions So Far

``` text
print()
type()
input()

int()
float()
str()
bool()

if
elif
else

for
while
range()
break
continue

in
and
or
not

len()

list methods:
append()
insert()
remove()
pop()
sort()
reverse()
count()
index()

tuple:
count()
index()

set:
add()
remove()
discard()
pop()

dictionary:
pop()
keys()
values()
items()
get()
clear()

string:
upper()
lower()
strip()
replace()
find()
count()
startswith()
endswith()
split()
join()

functions:
def
return
```

------------------------------------------------------------------------

# 🧭 What You've Learned So Far

``` text
01  Hello Python       ✅
02  Variables          ✅
03  Data Types         ✅
04  Operators          ✅
05  Input              ✅
06  Type Conversion    ✅
07  Conditionals       ✅
08  Loops              ✅
09  Lists              ✅
10  Tuples             ✅
11  Sets               ✅
12  Dictionaries       ✅
13  Strings             ✅
14  Functions          ✅
```

Current level:

``` text
Python Foundation
██████████████████████████████ 100%
```

Next:

``` text
15 — Function Masterclass
```

------------------------------------------------------------------------

# 📌 Git

Store this README in your repository root, for example:

``` text
Python-Beg/
├── 01-basics/
└── README.md
```

Then commit it:

``` bash
git add README.md
git commit -m "docs: add Python lessons 01-14 quick reference"
git push
```

This file is intended as a **quick revision sheet**, while the numbered
`.py` files remain your hands-on practice.
