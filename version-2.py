import random

random_number = random.randint(1, 10)
guessed = False

while not guessed:
 user_guess = int(input("guess a number between 1 and 10:"))

if user_guess == random_number:               
  print ("you win! you guessed the correct number")
  guessesd = True
else: 
  print("you lose!")
