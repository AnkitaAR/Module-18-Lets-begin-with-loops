n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
def hcf(x, y):
    while(y):
        x, y = y, x % y
    return x
print("The HCF of", n1, "and", n2, "is", hcf(n1, n2))   