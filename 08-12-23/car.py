class car:   
    def __init__(self,color,price,km):
        self.color=color
        self.price=price
        self.km=km
    def __gt__(self,others):
        if(self.price>others.price):
            return True
        else:
            return False
    def __add__(self,others):
        return (self.km+others.km)
c1=car("porsche",1000000,1000)
print("car1:Porsche-1000000,1000")
c2=car("grey",1800000,1500)
print("car2:audi-1000000,1000")
if(c1>c2):
    print("price of car1 is high")
else:
    print("price of car2 is high")
print("total kms of car1 & car2:",c1+c2)
