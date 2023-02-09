a=int(input())
b=int(input())
def gcd (a,b):
    for i in range(1,a+b):
        x=a+b-i+1
        if a%x==0 and b%x==0:
            return x
print(gcd(a,b))
