#day -> 07
#simple calculator with add, sub , mul and div 

class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        try:
            return self.a-self.b
        except Exception as e:
            print(e)
                
    def mul(self):
            return self.a*self.b
    def div(self):
        try:
            return self.a/self.b
        except Exception as e:
            print(e)


while True:
    n=int(input("enter your choice(1.give numbers,2.add,3.sub,4.mul,5.div,6.exit) : "))
    if n==1:
        a=int(input("enter your first number : "))
        b=int(input("enter your second number : "))
        cal=calculator(a,b)
    
    elif n==2:
        r=cal.add()
        print("result :",r)
    elif n==3:
        r=cal.sub()
        print("result: ",r)
    elif n==4:
        r=cal.mul()
        print("result: ",r)
    elif n==5:
        r=cal.div()
        print("result: ",r)
    
    elif n==6:
        print("quiting the calculator!!")
        break
    else:
        print("invalid number , try again ")

