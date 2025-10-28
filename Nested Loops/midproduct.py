n=int(input("Enter the number(should be more than three digits): "))
mid_digit_index=len(str(n))//2
nextdigit_index=mid_digit_index+1
mid_digit=str(n)[mid_digit_index]
product=int(mid_digit)*int(str(n)[nextdigit_index])
print("The middle digit is:", mid_digit)    
print("The product of the middle digit and the next digit is:", product)