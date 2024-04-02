#dictionary is always unodered
dict={"Aqeel": "A coder", 
      "degree":"BSCS", #degree is key and BSCS is value
      "list": [1,23,44,55] #we can use lists in dictionary 
      ,
      "dict2":{"Aqeel":"Student",
               "number":123}# Nested dictionary
}
# print(dict)
# print(dict["Aqeel"])
# # dictionary is mutable
# dict["list"]=[15,45,69] #cannot contain duplicate keys it updates the previous
# print(dict["list"])

# print(dict.keys())
# print(dict.values())
# # diff b/w get and simple
# print(dict["degree"])
# print(dict.get("degree"))
# actual diff
# print(dict["degree1"]) #it throws error
print(dict.get("degree1")) #it gives None

# print(dict["dict2"])
# print(dict["dict2"]["Aqeel"]) #access values of nested dictionary
