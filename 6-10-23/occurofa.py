listn=["feri","nitha","hana","sara","sana"]
count=0
print(listn)
a=input("Enter the letter required:")
for n in listn:
    for f in n:
        if f==a:
            count+=1
print("the number of",a,"is:",count)
