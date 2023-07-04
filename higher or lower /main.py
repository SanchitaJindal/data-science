import random
from art import logo,vs
from game_data import data
print(logo)
choice=True
score=0
def ans(a,b):
  if a["follower_count"]>b["follower_count"]:
    return "A"
  else:
    return "B"
def setup(a,b):
  global score
  a_name=a["name"]
  a_desc=a["description"]
  a_count=a["country"]
  b_name=b["name"]
  b_desc=b["description"]
  b_count=b["country"]
  print(f"Compare A: {a_name}, a {a_desc}, from {a_count}.")
  print(vs)
  print(f"Against B: {b_name}, a {b_desc}, from {b_count}.")
  guess=input("Who has more followers? Type 'A' or 'B': ")
  if guess==ans(a,b):
    score+=1
    print(f"You're right! Current score: {score}")
    c=random.choice(data)
    setup(b,c)
  else:
    print(f"Sorry,that's wrong.Final score {score}")
    return
a=random.choice(data)
b=random.choice(data)  
setup(a,b)