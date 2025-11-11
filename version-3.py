import random

limite = 6
random_number = random.randint(1, 10)
print(random_number)
guessed = False
user_guess = int(input("Enter a number between 1 and 10:"))
limite -= 1
 
while user_guess != random_number and limite > 1:
  user_guess =int(input("Enter a number between 1 and 10:"))
  limite -= 1
  if user_guess == random_number: 
      print("you win!")
      guessed = True
  else:
      print("you lose!")

