#resources complete
# money sufficient
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def suff_res(choice,MENU,resources):
    for i in MENU[choice]["ingredients"]:
        if MENU[choice]["ingredients"][i]>resources[i]:
            print(f"Sorry there is not enough {i}")
            return False
    return True
total=0.0
def money(quarters,dimes,nickels,pennies,choice,MENU):
    m=0.25*quarters+0.1*dimes+0.05*nickels+0.01*pennies
    if MENU[choice]["cost"]>m:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        return m-MENU[choice]["cost"]
while True:
    choice=input("What would you like? (espresso/latte/cappuccino):")
    if choice=="report":
        water=resources["water"]
        milk=resources["milk"]
        coffee=resources["coffee"]
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${total}")
    elif choice=="off":
        break
    else:
        if suff_res(choice,MENU,resources)==False:
            pass
        else:
            print("Please insert coins.")
            quarters=int(input("how many quarters?:"))
            dimes=int(input("how many dimes?:"))
            nickels=int(input("how many nickels?:"))
            pennies=int(input("how many pennies?:"))
            if money(quarters,dimes,nickels,pennies,choice,MENU)!=False and suff_res(choice,MENU,resources)==True:
                print(f"Here is ${money(quarters,dimes,nickels,pennies,choice,MENU)} in change.")
                print(f"Here is your {choice} ☕️. Enjoy!")
                for i in MENU[choice]["ingredients"]:
                    resources[i]-=MENU[choice]["ingredients"][i]
                total+=MENU[choice]["cost"]