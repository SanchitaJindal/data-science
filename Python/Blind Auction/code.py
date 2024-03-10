from art import logo
print(logo)
print("Welcome to the secret auction program.")
d={}
l=[]
name=input("What is your name?:")
bid=input("What is your bid?:")
l.append(int(bid[1:]))
d[name]=bid
choice=input("Are there any other bidders? Tyoe 'yes' or 'no'.\n")
while  choice!="no":
  name=input("What is your name?:")
  bid=input("What is your bid?:")
  d[name]=bid
  l.append(int(bid[1:]))
  choice=input("Are there any other bidders? Tyoe 'yes' or 'no'.\n")
maximum=max(l)
for key in d:
  if d[key]==("$"+str(maximum)):
    print("The winner is",key,"with a bid of",d[key])  