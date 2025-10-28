n=int(input("Enter the number of elements in the list: "))
strong_numbers=[]
for i in range(n):
    num=int(input("Enter a number: "))
    temp=num
    sum_factorial=0
    while temp>0:
        digit=temp%10
        factorial=1
        for j in range(1,digit+1):
            factorial=factorial*j
        sum_factorial=sum_factorial+factorial
        temp=temp//10
    if sum_factorial==num:
        strong_numbers.append(num)
print("The strong numbers in the list are:", strong_numbers)