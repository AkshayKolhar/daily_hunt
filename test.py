

l=[6,4,3,5,8]
for i in range(1,len(l)):    

    key=l[i]
    j=i-1

    while j>=0 and l[j]>key:
        l[j+1]=l[j]
        j-=1
    
    l[j+1]=key

print(l)

def divexp(a,b):
    assert a>0,"Error: a must be greater then zero "

    if b==0:
        raise ValueError("error : divison by zero is not valid")
    c=a/b
    return c

try:
    a=7 
    b=4
    resul=divexp(a,b)
    print(resul)

except AssertionError as ae:
    print(ae)
except ValueError as v:
    print(v)
except Exception as e:
    print(e)


class complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def __str__(self):
        sign="+" if self.imag>0 else "-"
        return f"{self.real} {sign} {abs(self.imag)}i"
    
def add_comp(c1,c2):
    return complex(c1.real+c2.real,c1.imag+c2.imag)

N=int(input(">> "))

if N<2:
    print("n must be greater then 2")
else:
    comp_l=[]
    for i in range(N):
        print("enter the comlex numbers")
        real=float(input("real>> "))
        imag=float(input("imag>> "))
        comp_l.append(complex(real,imag))

temp=comp_l[0]
for i in range(1,N):
    temp=add_comp(temp,comp_l[i])

print(temp)