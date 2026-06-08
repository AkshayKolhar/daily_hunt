#day -> 08 
#reversing a string 

def day81():
    st="akshay"
    r=""
    for l in reversed(st):
        r+=l
    print(r)
    s=''.join(reversed(st))
    print(s)

#counting vowels 
def day82():
    vowels="aeiou"
    while True : 
        st=input("Enter your string: ")
        if st=="exit":
            break
        else:
            r={}
            print("given word : ",st)
            for w in st:
                if w in vowels:
                    if w in r:
                        r[w]+=1
                    else:
                        r[w]=1
            print("vowels in word :",st)
            for w,c in r.items():
                print(f"{w}: {c}")

