print("Select your ride")
print("1.Bike")
print("2.Car")
choice1=int(input("Please enter your choice"))
if choice1==1:
    print("Please choose your bike")
    print("1. Scooty")
    print("2.Scooter")
    choice2=int(input("Please enter your choice"))
    if choice2==1:
        print("You have chosen a scooty")
    else:
        print("You have chosen a scooter")
else:
    print("Please choose your car")
    print("1. Sedan")
    print("2.XUV")
    choice3=int(input("Please enter your choice"))
    if choice3==1:
        print("You have chosen a Sedan")
    else:
        print("You have chosen a XUV")

