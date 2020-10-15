# Its a Guess The Number Game
import random

print('Enter Your Name:-')
name = input()
print('Hiii ' + name + 'Try to Guess the number between(1-20). (You Have 6 tries. Try as hard as you can. Good Luck)')
secretNum = random.randint(1,20)
#print(secretNum) For testing Purposes
for guessTaken in range(1,7):
    print('Enter Ur Guess:')
    guess = int(input())
    if guess < secretNum:
        print('LOW, Tries Left:' + str(6-guessTaken))
    elif guess > secretNum:
        print('HIGH, Tries Left:' + str(6-guessTaken))
    else :
        break
if guess == secretNum :
    print('Good Job ' + str(secretNum) + ' is Right Answer. BTW u Took ' + str(guessTaken) + ' Tries')
else:
    print('!!!!!!!!!!!!!!!!!!!!!0 Tries Left!!!!!!!!!!!!!!!!!!!!!!!!!')
