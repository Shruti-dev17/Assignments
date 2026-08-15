
#Print stars

for i in range(1,6):
    for j in range(1,i+1):
        print('*',end='')
    print()

# Roll a dice

import numpy as np
while True:
    print("Welcome to roll the dice")
    user=input("Please enter to roll the dice or press 'q' to quit: ")
    die= np.random.randint(1,7)

    if user == 'q':
        print("Thanks for playing, bye!")
        break
    elif user =='':
        print("the rolled number isssssssssssss :",die)
    else:
        print("Invalid choice. Try Again")

# find the no. of words with letter i as there 2nd letter in the list and store them.

names=['rita','gita','siita','minam','mina','yn','younghi','mingyu','kats','harshita','abha']
count=0
inames=[]
for c in names:
    if c[1]=='i':
        count=count+1
        inames.append(c)

print("No. of names with i in 2nd position",count)
print("names with i in 2nd position:",inames)

# GUESS THE NUMBER IN 10 CHANCE!!!!

num = np.random.randint(1,50)

for i in range(1,11):
    guess=int(input(f"Guess the number between 1 to 50.({i}/10):"))
    if guess == num:
        print(f"{guess} is the correct guess!!you got it in {i} guess!!")
        break

    elif guess not in range(1,50):
        print("Invalid input!!! The value must be between 1 to 50.")
        print("Try again:")
    
    else :
        if i == 10:
                print("Oops...You couldn't guess the right number!!")
                print("The correct ans is :",num)
        else:
            if (guess > num) :
                print(f"Wrong guess!! try lower:")
            else:
                print(f"Wrong guess!! try heigher:")           
            
print("Thankyou for playing!!")