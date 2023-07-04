from art import logo,vs
from game_data import data
import random
score=0
choice=True
print(logo)
x=random.randint(0,len(data))
y=random.randint(0,len(data))
if x!=y:
  a=data[x]
  b=data[y]
  while choice==True:
    a_name=a["name"]
    a_des=a["description"]
    a_count=a["country"]
    b_name=b["name"]
    b_des=b["description"]
    b_count=b["country"]
    print(f"Compare A: {a_name}, a {a_des}, from {a_count}.")
    print(vs)
    print(f"Against B: {b_name}, a {b_des}, from {b_count}.")
    guess=input("Who has more followers? Type A or B: ")
    if a["follower_count"]>b["follower_count"]:
      ans='A'
    else:
      ans='B'
    if guess==ans:
      score+=1
      print(f"You're right! Current score: {score}.")
      a=data[y]
      y=random.randint(0,len(data))
      b=data[y]
      if a==b:
        y=random.randint(0,len(data))
        b=data[y]
    else:
      choice==False
  else:
    print(f"Sorry!That's Wrong. Final Score={score}")
else:
  y=random.randint(0,len(data))