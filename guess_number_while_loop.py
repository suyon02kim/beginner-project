print("Welcome to guess the right number. Where you get to choose how many times you want to play and you will be choosing the upper bound of the range.")

u_range = input("Choose the upper bound of the range: ")
print("Try to guess a number between 0 to " + u_range )
times = int(input("How many times would you like to try? "))

import random 
guess_num = (random.randint(0,int(u_range)))

n = 1 
while n <= times:
  user_guess = int(input("What is your guess? "))
  if guess_num == user_guess:
    print("You guessed it right!")
    break
  else: 
    print("Guess again.")
  n = n + 1
