a, b, c = map(int, input().split())
sum=a+b+c
if a==180 and b==0 and c==0:
    print("No")
elif a==0 and b==180 and c==0:
    print("No")
elif a==0 and b==0 and c==180:
    print("No")
elif a==0 and b==0 and c==0:
    print("No")
elif a>0 and b>0 and c==0:
    print("No")
elif a==0 and b>0 and c>0:
    print("No")
elif a>0 and b==0 and c>0:
    print("No")
elif sum<0:
    print("No")
elif a<0 or b<0 or c<0:
    print("No")
elif sum==179:
    print("No")
elif sum<=180:
    print("Yes")
elif sum>180:
    print("No")
elif sum>360:
    print("No")

