string=input("Enter your sentence")
count=1
for i in range(len(string)):
    if (string[i]==' '):
        count+=1
print("Count :",count)