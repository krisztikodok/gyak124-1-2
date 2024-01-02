#number guessing game
import random

truth=False
secret=random.randint(1,100)
guess=int(input("Enter a nr between 1 and 100: "))
if guess==secret:
  truth==True
else:
  truth

if truth==True:
  print("You guessed it!")
else:
  print(f"You didn't guess it, it's {secret}")