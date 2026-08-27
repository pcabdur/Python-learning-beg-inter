numbers = {10, 20, 30, 40}

print(numbers)
print(type(numbers))

'''the thing is like we can remove duplicates and we can use some function in this also bruh and more '''
numbers = {10, 20, 20, 30, 30, 30}

print(numbers)

#4. Sets are unordered
names = ["Abdur", "Ali", "Ahmed","asm"]

# you can add elemts bruh but u cant acces tthem like this bruh we cant 
# like this names[2]
# this throughts errprs bruh 



names.add("Ahmed appa")
names.add("bruh")

print(names)

# remove 

names.remove("Ali")

print(names)

#    discard()

'''
remove()  → error if missing
discard() → doesn't care if missing
'''

names.discard("Rahul")

print(names)

# pop( also bruh)



item = names.pop()

print(item)
print(names)

# also len ()

print(len(names))

# also in 

print("abdur"in names)

for name in names:
    print(name)

myfavs={"asm","pca","pcasm"}

all_names=myfavs | names
print(all_names)

comm=myfavs & names

print(comm)

defs=myfavs - names
# also this ^ not in both this mean   bruh


 # so bruh this  we can conver this to set bruh like set() that all bruh 

numbers = [10, 20, 20, 30, 30, 40, 40, 40]
unique_numbers = set(numbers)


'''
|              | List       | Tuple            | Set                        |
| ------------ | ---------- | ---------------- | -------------------------- |
| Syntax       | `[]`       | `()`             | `{}`                       |
| Ordered      | Yes        | Yes              | No positional order        |
| Mutable      | Yes        | No               | Yes                        |
| Duplicates   | Yes        | Yes              | **No**                     |
| Indexing     | Yes        | Yes              | No                         |
| `in`         | Yes        | Yes              | Yes                        |
| Main purpose | Collection | Fixed collection | Unique values / membership |

'''