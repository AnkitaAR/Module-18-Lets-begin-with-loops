u=int(input("Enter the upper limit"))
l=int(input("Enter the lower limit"))
print("Prime number between ",l," and ",u," are :")
for i in range(l,u+1):
    if i>1:
     for j in range(2,i):
        if i%j==0:
           break
     else:
           print(i)