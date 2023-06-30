from art import logo

print(logo)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


print()
first = eval(input("What's the first number?: "))
print("+\n-\n*\n/\n")
choice = "y"
while choice == "y":
    operation = input("Pick an operation: ")
    second = eval(input("What's the next number?: "))
    if operation == "+":
        ans = add(first, second)
        print(first, operation, second, "=", ans)
        first = ans
    elif operation == "-":
        ans = subtract(first, second)
        print(first, operation, second, "=", ans)
        first = ans
    elif operation == "*":
        ans = multiply(first, second)
        print(first, operation, second, "=", ans)
        first = ans
    elif operation == "/":
        ans = divide(first, second)
        print(first, operation, second, "=", ans)
        first = ans
    print("Type 'y' to continue calculating with", ans,
          ",or type 'n' to start a new calculation: ")
    choice = input()