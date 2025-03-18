li = [1,3,6]

print(li)

li [0] = 10

print(li)

lis = ["Ronaldo","Subah","Neymar"]

print(lis)

# Access list item
lis = ["Ronaldo","Subah","Neymar"]
print(lis[0])

# Change List Items

lis = ["Ronaldo","Messi","Neymar"]
lis [1] = "Rodrygo"
print(lis)

# Add list items

# (Insert)

lis = ["Messi","Ronaldo","Neymar",]
lis.insert(2,"Suarez")
print(lis)

# (append)

lis = ["Messi","Ronaldo","Neymar",]
lis.append("Suarez")
print(lis)

# Remove list items

# (Remove)
lis = ["Messi","Ronaldo","Neymar",]
lis.remove("Neymar")
print(lis)

# Remove Specified Index pop ()
lis = ["Messi","Ronaldo","Neymar",]
lis.pop(0)
print(lis)

# Remove the last item:
lis = ["Messi","Ronaldo","Neymar",]
lis.pop()
print(lis)

# Clear the list content:
lis = ["Messi","Ronaldo","Neymar",]
lis.clear()
print(lis)

# Remove the first item:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


# You can loop through the list items by using a for loop:

LoopList = ["Messi","Neymar","Suarez"]

for x in LoopList:
    print(x)

# Use the range() and len() functions to create a suitable iterable.

for x in range(len(LoopList)):
    print(x)
    
