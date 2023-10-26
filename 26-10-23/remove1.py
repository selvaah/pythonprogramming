list=[5,20,29,57,81,74]
print("orginal list")
print(list)
for i in list:
    if i%2==0:
        list.remove(i)
print("list after removing even number")
print(list)
