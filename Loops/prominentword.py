text=input("Enter a sentence:")
text=text.split()
largewordlength=0
for word in text:
    wordlen=len(word)
    if wordlen>largewordlength:
        largestword=word
        largewordlength=len(word)
    

for word in text:
    if largewordlength==len(word):
        print(word," is the largest word")


