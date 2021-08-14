"""Number guessing game developed using Python"""

import random      #Importing random function   

num=random.randint(1,100)   #Random value will be selected between 1 to 100

p1=input("Player 1, Enter your name : ")
p2=input("Player 2, Enter your name : ")
pp1=1
pp2=1

#Player1 turn
guess=int(input("Player 1, Its your turn to guess a number between 1 to 100 : "))

#Logic for checking whether the guesse number is correct or not   
while(guess!=num):
    if(guess<num):
        print("Guess is too low")
    else:
        print("Guess is too high")
    guess=int(input("Take another guess : "))
    pp1+=1
print("Your guess is correct and your attempts are : ",pp1)

#Player2 turn
num=random.randint(1,100)   #Random value will be selected between 1 to 100
guess=int(input("Player 2, Its your turn to guess a number between 1 to 100 : "))

#Logic for checking whether the guesse number is correct or not
while(guess!=num):
    if(guess<num):
        print("Guess is too low")
    else:
        print("Guess is too high")
    guess=int(input("Take another guess : "))
    pp2+=1
print("Your guess is correct and your attempts are : ",pp2)

print("\nGame Summary:\nPlayer 1 score : ",pp1,"\nPlayer 2 score : ",pp2)
if(pp1>pp2):
    print("\nCongradulations ",p2," you have won the game")
elif(pp1<pp2):
    print("\nCongradulations ",p1," you have won the game")
else:
    print("\nGame is Draw")
print("\nThank you for playing the game")

    