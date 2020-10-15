# Its a Guess The Number Game
import random

print('Name')
name = input()
print('Hiii ' + name + ' Guess the number(1-20). (6 tries)')
secretNum = random.randint(1,20)
print(secretNum)
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
