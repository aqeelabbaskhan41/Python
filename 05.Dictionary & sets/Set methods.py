s={3,5,4,75,3,743,434,4367}
s.add(9)
# s.add([232]) #we cannot add list into set
s.add((43,6,95,7)) #It can add tuples into set
# s.add({"a":"erorr"}) we cannont add dictionary into set
print(s)
print(len(s)) #it tells the length of set
s.remove(743) #It removes the given number from the set
print(s)

s.pop() #It removes the random item from set
print(s)

# s.clear() #It clears the whole set
# print(s)

s.union() #it gives union of set
print(s)

s.intersection()#It gives intersection of the set
print(s)


