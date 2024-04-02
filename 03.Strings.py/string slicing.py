name="Aqeel"
print(name[0]) #index accessing
print(name[2])
print(name[4])
print(name[-5]) #negative indexing -1 will be starting bcz 
# 0 is positive from starting if zero in -ve then it make confusion

#Slicing  mean tukry string k
print(name[0:3]) #012 not till 3
print(name[:5])#if statring not given then it takes 0
print(name[2:])#it starts from index 2 to end

#Slicing with skip value 
a= "Aqeel is Good"
print(a[1:8:1]) #jumping vl is 1
print(a[0::2]) #jumping value is 2]
