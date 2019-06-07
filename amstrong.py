a = int(input())  
b= 0  
c =a 
while c> 0:  
   d = c % 10  
   b +=d ** 3  
   c //= 10  
  
if a== b:  
   print("yes")  
else:  
   print("no")
