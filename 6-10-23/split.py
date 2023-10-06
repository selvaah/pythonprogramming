a=str(input("Enter the line:"))
b=str(input("Enter the word to count:"))
list=a.split()
count=0
for n in list:
        if n==b:
            count=count+1
print("number of",n,"is",count)
