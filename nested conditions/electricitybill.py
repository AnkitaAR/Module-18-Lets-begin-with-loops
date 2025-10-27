units=input("Enter the electricity units : ")
units=float(units)
if units<50:
    amount=units*2.60
    surcharge=25
elif units<=100:
     amount=130+((units-30)*3.25)
     surcharge=35
elif units<=200:
    amount=130+162.5+((units-100)*5.26)
    surcharge=45
else:
    amount=130+162.5+526+((units-200)*8.45)
    surcharge=75

amount=amount+surcharge
print("Electricity bill:",amount)
