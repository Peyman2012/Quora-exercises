a=input("")
c1=a[0]
c2=a[1]
c3=a[2]
c4=a[3]
c5=a[4]
G=0
R=0
Y=0
if c1=='G':
    G=G+1  
elif c1=='Y':
    Y=Y+1  
else:
    R=R+1
    
if c2=='G':
    G=G+1  
elif c2=='Y':
    Y=Y+1  
else:
    R=R+1 

if c3=='G':
    G=G+1  
elif c3=='Y':
    Y=Y+1  
else:
    R=R+1 
    
if c4=='G':
    G=G+1  
elif c4=='Y':
    Y=Y+1  
else:
    R=R+1   
    
if c5=='G':
    G=G+1  
elif c5=='Y':
    Y=Y+1  
else:
    R=R+1
    
if R>=3 or (Y>=2 and R>=2) or G==0:
    print("nakhor lite")
else:
    print("rahat baash")
