cause=input("Is it a medical cause ?(Y/N):")

if cause.upper()=='N':
    attendance=input("Enter your attendance percentage:")
    attendance=int(attendance)
    if attendance>75:
        print("You can appear for the exam")
    else:
         print("You can not appear for the exam")

else:
    print("You can appear for the exam")