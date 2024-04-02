s=set()
s.add(20)
s.add(20.0) #20 and 20.0 are equal so it considered as one value
s.add("20")
print(len(s))
print(type(s))