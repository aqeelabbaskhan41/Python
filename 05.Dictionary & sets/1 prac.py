dic={ "acha":"Best",
    "bura":"Bad",
    "bara":"Big",
    "nafrat":"Hate",
    "pyar":"Love"

}
print(dic.keys())
a=input("Enter any key to find its meaning:")
# print(dic.[a])#it will give error if not present key entered
print("The meaning of ",a,"is", dic.get(a))
