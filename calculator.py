#python calculator 

operator = input("Enter an operator (+ - / *): ")
x = float(input("Enter your 1st number: "))
y = float(input("Enter your 2nd number: "))

def result(a, b):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "/":
        return a / b
    elif operator == "*":
        return a * b
    else:
        return "Select an operator"

print(result(x, y))