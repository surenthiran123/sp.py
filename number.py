n1=input();
n2=input();
n3=input();
Largest = n1
if Largest < n2:
        if n2 > n3:
            print(n2,"is Largest")
        else:
            print(n3,"is Largest")
elif Largest < n3:
        if n3 > n2:
            print(n3,"is Largest")
        else:
            print(n2,"is Largest")
else:
        print(n1,"is Largest")
