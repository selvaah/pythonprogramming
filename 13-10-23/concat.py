d1={1:5,2:6}
d2={3:7,4:8}
d3={}
print("The first dictionary is:")
print(d1)
print("The second dictionary is:")
print(d2)
for d in(d1,d2):d3.update(d)
print("The concatenate dictionary is:")
print(d3)
