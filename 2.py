a=input()
b=input()
c=a 
d=b 
a = a[::-1]
a=int(a)
b = b[::-1]
b=int(b)
if a>b:
    print(d ,"<", c)
elif a<b:
    print(c ,"<", d)
else:
    print(c ,"=", d)
