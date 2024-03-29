from art import logo
import random
print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
num=random.randint(1,100)
diff=input("Choose a difficulty. Type 'easy' or 'hard':")

if diff=="easy":
  t=10
else:
  t=5
for i in range(t,0,-1):
  print(f"You have {i} attempts remaining to guess the number.")
  guess=int(input("Make a guess:"))
  if guess<num:
    print("Too low.")
    if i==1:
      print("You've run out of guesses, you lose.")
      break
    else:
      print("Guess again.")
  elif guess>num:
    print("Too high")
    if i==1:
      print("You've run out of guesses, you lose.")
      break
    else:
      print("Guess again.")
  else:
    print(f"You got it! The answer was {num}")
    break