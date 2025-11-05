import random

play = True

while play:

  limit = 6
  num = random.randint(1, 100)
  guesses_made = []
  # print(num)
  
  guess = int(input("Enter a number between 1 and 100: "))
  guesses_made.append(guess)
  
  while guess != num and limit > 1:
    if guess > num:
      print("You guessed too high!")
    elif guess < num:
      print("You guessed too low!")
    limit -= 1
    print("Incorrect.")
    print("You already guessed %s" % (guesses_made))
    print("You have %s guesses left." % (limit))
    guess = int(input("Guess again: "))
    guesses_made.append(guess)
  
  
  if guess == num:
    print("Correct. You win!")
  else:
    print("You lose!")
  
  response = input("Would you like to play again? (y/n): ")
  if response == "y":
    play = True
  else:
    play = False
