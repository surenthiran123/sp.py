a,b=input().split()
c=int(a)
d=int(b)
for i in range(c+1,d): 
  n=0
  for j in range(1,d):
    if(i%j==0):
      n=n+1
  if(n==2):
    print(i,end=" ")
