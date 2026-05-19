#day ->04
#simple ATM machine 
class ATM:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def __str__(self):
        return f"username: {self.name}\nbalance: {self.balance}"

password=1234 
def day41():
    while True:
        name=input("enter your name: ")
        input_pass=int(input("enter your password: "))
        if input_pass==password: 
            bgk=ATM(name,1200)
            print(bgk)
            break
        else:
            print("incorrect password")

#student grade 
class grade:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        self.grade=""
    def anaylize(self):
        if self.marks>=90:
            self.grade="A"
        elif self.marks>=80:
            self.grade="B"
        elif self.marks>=65:
            self.grade="C"
        elif self.marks>=45:
            self.grade="D"
        else:
            self.grade="E"
    def result(self):
        self.anaylize()
        print(f"name : {self.name}\ngrade: {self.grade}")
a=grade("akshay",23)
a.result()

        
        
        
    
        



