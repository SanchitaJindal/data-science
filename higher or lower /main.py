from art import logo,vs
from game_data import data
import random
score=0
ans=True
while ans==True:
  print(logo)
  x=random.randint(0,len(data))
  y=random.randint(0,len(data))
  while x==y:
    y=random.randint(0,len(data))
  if x!=y:
    a=data[x]
    b=data[y]
    print("Compare A: {a[name]}, a {a[description]}, from {a[country}.")
    print(vs)
    print("Against B: {b[name]}, a {b[description]}, from {b[country}.")

