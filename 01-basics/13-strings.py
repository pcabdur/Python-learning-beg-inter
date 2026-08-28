name = "Abdur"

print(name[:3])
print(name[2:])
print(name[:])

print(name[::-1])
message = "bruh wth is this haha "
print(len(message))

print(name.upper())

print(name.lower())

# ther a function called strip( ) thsis is used for to remove white space in the frount and end of the string bruh fr 

message = "I love Java"

message = message.replace("Java", "Python")

print(message)


# this is uwed in some plaves for us to make some probele like to find and replavce bruh so we need ro learn tis haha


text = "Hello Python"

print(text.find("Python")) 

'''

H e l l o   P y t h o n
0 1 2 3 4 5 6

'''

text = "python python python"

print(text.count("python"))


# this is a startwith fucnton use to find whethr this function start thwoi shis or nah bruh lie thay 


url = "https://example.com"

print(url.startswith("https"))

# same btuh but end wiht this ? like thay bruh thay all 
filename = "model.py"

print(filename.endswith(".py"))


# so we are goonna say wher it in in this or nah bruh that all 

message = "I am learning Python"

print("Python" in message)


# this is very very impirtan for me this is used to get all word into splite to get them as a splits of words so

sentence = "I am learning Python"

words = sentence.split()

print(words)

'''
output:

['I', 'am', 'learning', 'Python']

'''

data = "Abdur,20,India"

result = data.split(",")

print(result)

# we cans use a condition foo this to amke this work like we can use any thoing afor me to as we need bruh wth i am typing this is night haha i was in a drink state i guess haha i can t stop typin burh get this out od ur head and moce nest bruh haha 


words = ["I", "love", "Python"]

sentence = " ".join(words)

print(sentence)

# by usig split( ) and alsi we can join the splited words as one bruh fr 


name = "Abdur"
age = 20

print(f"My name is {name} and I am {age} years old.")

'''
The f means:

This string can contain expressions inside {}.

'''

age = 20

print(f"Next year I will be {age + 1}")

x = 10
y = 20

print(f"Sum = {x + y}")

user = {
    "name": "Abdur",
    "age": 20
}

print(f"Name: {user['name']}")
print(f"Age: {user['age']}")



e=input("give me ut email gng")
if "@" in e and "." in e:
    print("valid ")
else: 
    print( "hell nah getfo burh ")

Fname="abdur"
Lname="rahman"
Byear=int(input())

print(f"gendrated username :{Fname}_{Lname}{Byear}")


# by using these types of cunction we can remove space in that sing i mean we can like thiese 

'''
Remove normal spaces everywhere

text.replace(" ", "")

Remove all spaces, tabs, and newlines

"".join(text.split())

Reduce extra spaces to just one

" ".join(text.split())

Only remove outer edges (trim)

text.strip()


'''


