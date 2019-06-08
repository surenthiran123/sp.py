n1,n2=input("").split()
n1,n2=(int(n1),int(n2))
for i in range(n1,n2):
     a=0 
     b=i
     while(i!=0):
          r=i%10;
          a=a+r*r*r;
          i//=10;
     if(b==a):
        print(b,end=" ")
