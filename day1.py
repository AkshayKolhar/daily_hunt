#day 1 
import datetime 
date=datetime.date.today()
time=datetime.datetime.now().time()

# q1:printing the age , by taking input name and age.
def det(name,age):
    print(f"Hello {name}, you are {age} years old!! ")
def detials():
    while True:
        name=input("Enter your name: ")
        age=int(input("enter your age(should be +ve): "))
        if age>0:
            det(name,age)
            break
        else:
            print("Please enter a valid age!!")

#q2: calculating the bill for electricity by taking input house no and units consumed.

class bill:
    def __init__(self,HN,units):
        self.HN=HN
        self.units=units
        self.bill_cost=0
    
    def bil_cal(self):
        self.bill_cost=self.units*8
    
    def billing(self):
        print(f"billing on {date}\nat {time}\nHouse no: {self.HN}\nthis month:\n electricity units :{self.units}\n bill cost is : {self.bil_cal()}\nThank you")

def ent_det():
    
    hn=int(input("enter the house no: "))
    units=int(input("enter the electricity units: "))
    b=bill(hn,units)
    b.billing()

ent_det()