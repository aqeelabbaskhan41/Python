dict={"Aqeel": "A coder", 
      "degree":"BSCS", #degree is key and BSCS is value
      "list": [1,23,44,55] ,# we can use lists in dictionary 
      1:34,
      "dict2":{"Aqeel":"Student",
               "number":123}# Nested dictionary
}
print(dict.keys())
print(list(dict.keys())) #it type cast the keys into list
print(dict.values())#It prints values of keys

print(dict.items())#It prints the dictioary contents in pairs form
print(list(dict.items()))#it convert the item into list

update_dict={"niazi":"Imran Khan",
             1:22 #Value of key 1 become 22 from 34 bcz it uopdates the previous value
}
dict.update(update_dict)#It adds the new dictionary into old dictionary
print(dict)

print(dict["list"])
print(dict.get("list")) #Here both works same
#Major difference
# print(dict["list1"])]# It throws key error 
print(dict.get("list1"))# It returns none