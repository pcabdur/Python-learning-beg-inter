##this is a list bruh 

names2 = ["Abdur", "Ali", "Ahmed"]

##this is a tuple bruh 

names1 = ("Abdur", "Ali", "Ahmed")

## basically oyu cant cnage or modfy the vales that all bruh 

numbers = (10, 20, 30, 40)

print(numbers)
print(type(numbers))

names = ("Abdur", "Ali", "Ahmed")

print(names[0])
print(names[1])
print(names[-1])

numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])

## 11. Why would we use a tuple?
##  Here's the real question.
#  Suppose you have a coordinate:
# so we cant or dont wneed to change that ting so it might get 


'''
| Feature    | List | Tuple  |
| ---------- | ---- | ------ |
| Syntax     | `[]` | `()`   |
| Ordered    | Yes  | Yes    |
| Indexing   | Yes  | Yes    |
| Slicing    | Yes  | Yes    |
| Mutable    | Yes  | **No** |
| `append()` | Yes  | No     |
| `remove()` | Yes  | No     |
| `pop()`    | Yes  | No     |
| `count()`  | Yes  | Yes    |
| `index()`  | Yes  | Yes    |
| `len()`    | Yes  | Yes    |
'''

person = ("Abdur", 20, "India")

name, age, country = person
print(name,age,country)
x=100
y=2333
x,y=y,x
print(x,y)


point=(10,20)
x,y=point
print(x)
print(y)
print("sum:",x+y)
print("por",x*y)


# we can use enumerate  function

names = ("Abdur", "Ali", "Ahmed")

for index, name in enumerate(names):
    print(index, name)