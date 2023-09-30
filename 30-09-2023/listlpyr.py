print ("Print leap year between two given years")
CYr=int(input("Enter the current year:"))
LYr = int(input("Enter last year:"))
print ("List of leap years:")
for year in range(CYr, LYr):
  if (year % 4==0):
    print (year)
