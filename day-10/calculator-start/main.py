from art import logo

print(logo)


# Add
def add(num1, num2):
    return (num1 + num2)


# Subtraction
def sub(num1, num2):
    return (num1 - num2)


# Multiplication
def mul(num1, num2):
    return (num1 * num2)


# Division
def div(num1, num2):
    return (num1 / num2)


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

num1 = int(input("What's the first number?: "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation: ")
num2 = int(input("What's the next number?: "))
calc = operations[operation_symbol](num1, num2)
print(f"{num1} {operation_symbol} {num2} = {calc}")
