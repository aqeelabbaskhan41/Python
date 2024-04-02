# this="        Aqeel is a good boy"
# print(this)
# print(this.strip()) #Strip removes the extra spaces from the string

def remove_strip(string,word):
    a= string.replace(word, "")
    return a.strip()

this="        Aqeel is a good boy    "
s=remove_strip(this,"Aqeel")
print(s)