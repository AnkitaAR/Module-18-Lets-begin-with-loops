text=input("Enter the text")
char=input("Enter the character to be searched")
i=0
charcount=0
while(i<len(text)):
    if char==text[i]:
        charcount=charcount+1
    i=i+1
print(char," appears ", charcount ," times in the text ",text)
