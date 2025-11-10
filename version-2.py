import random

random_number = random.randint(1, 10)
print(random_number)
guessed = False
user_guess = int(input("Enter a number between 1 and 10:"))
 
while user_guess != random_number:
  user_guess =int(input("Enter a number between 1 and 10:"))
  if user_guess == random_number: 
      print("you win!")
      guessed = True
  else:
    print("you lose!")
