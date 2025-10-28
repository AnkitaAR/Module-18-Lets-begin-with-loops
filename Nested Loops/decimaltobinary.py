n=int(input("Enter the number "))
binary=""
while n>0:
    rem=n%2
    binary=str(rem)+binary
    n=n//2
print("The binary equivalent is:", binary)