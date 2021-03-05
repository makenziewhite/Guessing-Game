# This is a guess the number game.
import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 100)
print('Well, ' +myName+', I am thinking of a number between 1 and 100')

for guessesTaken in range(4):
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('your guess is too low.')

    if guess > number:
        print('your guess is too high')

    if guess == number:
        break
    
if guess == number:
    guessesTaken=str(guessesTaken + 1)
    print('Good job! You guessed my number in' + guessesTaken + ' guesses!')


if guess != number:
              number = str(number)
              print('nope, the number I was thinking of was ' + number + '.')

import random
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
myNumber = random.randit(smaller, larger)
count = 0
while True:
   count += 1
   if userNumber < myNumber:
       print("Too small")
   elif userNumber > myNumber:
       print("Too large")
   else:
       print("Congratulations! You've got it in", count, "tries!")
       break
