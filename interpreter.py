def math_intepreter(a,b,c):
    a = float(a)
    c = float(c)
    
    if b == "+":
        return a + c
    elif b == "-":
        return a - c
    elif b == "*":
        return a * c
    elif b == "/":
        return a / c
    else:
        return "Error"

def main(): 
    numbers = input("Expression: ")
    x, y, z = numbers.split(" ")

    print(math_intepreter(x,y,z))
    
main()
