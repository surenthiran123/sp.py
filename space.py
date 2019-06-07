n1,n2=[int(n1) for n1 in input().split()]
x=range(n1,n2)
list=[]
for y in x:
    if((y>n1) and (y<n2)):
        if(y%2!=0):
            list.append(str(y))
z=' '.join(list)
print(z)
