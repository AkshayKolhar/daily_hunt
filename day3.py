#day-> 03
# q1-> checking the candidate .whether he is eligible for vote or note
class vote:
    def __init__(self,age,resident,mental_cond):
        self.age=age
        self.resident=resident
        self.mental_cond=mental_cond
    
    def check_age(self):
        if self.age>18:
            return True
        else:
            return False
    def ch_res(self):
        if self.resident:
            return True
        else:
            return False
    def ch_MC(self):
        if self.mental_cond:
            return True
        else:
            return False
    def check(self):
        self.check_age()
        self.ch_res()
        self.ch_MC()
        if self.check_age() and self.ch_res() and self.ch_MC():
            print("he/she is eligible for voting in our country")
        else:
            print("he/she is not eligible for voting in out country")

def d31():
    age=int(input("enter your current age: "))
    res=input("are u resident of india y/n: ")
    mc=input("are u fit for taking decision for election y/n: ")
    if res=="y":
        res=True
        if mc=="y":
            mc=True
        else:
            mc=False
    else:
        res=False
    p=vote(age,res,mc)
    p.check()

#q2-> password verifier 
class password:
    def __init__(self,name):
        self.name=name
        self.password=" "
        self.lists={
            "akshay":"aks077",
            "siddu":"sidd22"
        }
    
    def create_pass(self):
        self.password=input("Create the password: ")
        
        self.lists[self.name]=self.password

    def enter(self,input_password):
        if input_password==self.lists[self.name]:
            for n,p in self.lists.items():
                if n==self.name:
                    print(f"successfully logined")
                    print(f"{n} : {p}")
        else:
            return False
def d32():
    name=input("enter your name: ")
    user=password(name)
    while True:
        print("press 1 for create a password\npress 2 for login\npress 3 for exit ")
        n=int(input("your chioce (1/2): "))

        if n==1:
            user.create_pass()
            print("successfully created")
        elif n==2:
            print("entering to the login page ")
            input_pass=input("please enter password: ")
            user.enter(input_pass)
            
            print("thank you")
        elif n==3:
            print("thank you for coming ")
            break
        else:
            print("Invalid option read instruction properly ")

        