for i in range(5):
    print("bruh wassup 5 times hahah ")
print(range(4))

for i in range(2,7):
    print(i)
for i in range(0,10,2):
    print(i)
#reverse rbuh
for i in range(10, 0, -1):
    print(i)
name="A bdur"
for let in name:
    print(let)
### while looop
count = 1

while count <= 5:
    print(count)
    count += 1

for i in range(4):
    if i ==2:
        break
    print(i)

for i in range(5):
    if i == 2:
        continue

    print(i)
    
count=0
num=44
while (True):
    gess=int(input(" guess a numbbruh "))
    count+=1
    if num == gess:
        break
    elif num>gess:
        print(" bruh low man ")
    elif num<gess:
        print("high bruh")
    else:
        print( " are u dumb bruh fr? gng?")
print(" u used this much haha to noob ",count)