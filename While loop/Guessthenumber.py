import random
print("Welcome to game GUESS THE NUMBER!")
print("Once you guess the number,I will tell you how far/close are you to the correct number ")
print("You have 20 trials")
min=-1000
max=1000
correct=random.randint(-1000,1000)
trialno=1
while trialno<=20:
  guess=input("Guess a number between -1000 and 1000 :")
  guess=int(guess)
  if guess>1000 and guess<-1000:
    print("Please enter a number within the range of -1000 and 1000")
  else:
   temp=correct-guess
   temp=abs(temp)
   if temp>1000: 
    print("Your guess is very very far")
   elif temp>100 and temp<=1000:
    print("Your guess is very far")
   elif temp<=100 and temp>50:
    print("Your guess is far")
   elif temp<=50 and temp>3:
    print("Your guess is close")
   elif temp<=3 and temp>0:
    print("Your guess is very close")
   elif temp==0:
    print("JACKPOT!!!THE NUMBER WAS",correct)
    break
  trialno+=1
  trialleft=20-trialno
  print("You are left with ",trialleft,"trials")
if trialno==21:
  print("You lost")