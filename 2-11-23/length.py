listofWords = list(input("Enter the list of words:").split())
maxLength = len(listofWords[0])
word = listofWords[0]
for i in listofWords:
    if(len(i) > maxLength):
        maxLength = len(i)
        word = i
print("The longest word :")
print(word)
print("The length of longest word :")
print(len(word))

