name=["abdur","pcas","lolol"]
print(name)
print(type(name))


numbers = [10, 20, 30, 40, 50]

print(numbers)

data = ["Abdur", 20, 185.5, True]

print(data)

print(name[2])

print(name[-1])

print(name[-2])

# if we change what happend?


names = ["Abdur", "Ali", "Ahmed"]

names[1] = "Rahul"

print(names)

print(len(names))
#     append
names.append("asm")
print(names)
#    insert
names.insert(1,"pca")
print(names)

#  remove

names.remove("Abdur")

names.append("bruh")

#   pop

names.pop()
# can use index to pop elemts like names.pop(2)

## in keyword 

print( "pca" in names)

if "asm"in names:
    print("found")

faves=["perfect","asm",5,"wallhi","nah"]
print(faves)
print(faves[0])
print(faves[-1])
print(len(faves))

languages = ["Python", "Java", "C++"]

print(" give me some names of the products")
na=[]
for i in range (4):
    na.append(input())
print(na)
print( "total names",len(na))

## a new way bruh 

for i,na1 in enumerate(na):
    print(i+1,na1)


#sort lets learn sort function bruh

numbers = [50, 10, 40, 20, 30]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
names = ["Abdur", "asm", "Ahmed"]

names.reverse()

print(names)

numbers = [10, 20, 10, 30, 10]

print( numbers.count(10))

print(numbers.index(20))