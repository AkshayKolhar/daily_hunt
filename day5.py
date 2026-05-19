import time as t
#day -> 05
#printing tables upto n 


class table:
    def __init__(self,n):
        self.n=n
    def givetable(self):
        for i in range(1,11):
            print(f"{self.n} X {i} = {self.n*i}")
    
    def ntable(self):
        for i in range(1,self.n+1):
            for j in range(1,11):
                print(f"{i} X {j} = {j*i}")
        print(" ")
    

   
def day51():
    while True:
        n=int(input("enter your number : "))
        m=input("do u want nth table or upto nth table (y/n): ")
        tab=table(n)
        if m=="y":
            
            tab.givetable()
        else:
            tab.ntable()


class Timer:
    def __init__(self,n):
        self.n=n
    def stopwatch(self):
        print("starting time>> ")
        for i in range(self.n):
            print(f"{i} sec")
            t.sleep(1)
        print("Time Up")
def day52():
    s=Timer(10)
    s.stopwatch()
day52()



        


        
