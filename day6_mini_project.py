#safe calculator that never crashes
def calculator(num1, operator, num2):
    try:
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1*num2
        elif operator == "/":
            if num2 == 0:
                return "ERROR: cannot divide by 0"
            return num1/num2
        else:
            return "ERROR: Unknown oprator"
    except:
        return "ERROR: Something went wrong"
    
print("=" * 30)
print("   Safe Calculator")
print("=" * 30)
print()

while True:
    print("Enter 'EXIT' to quit")

    num1 = input("Enter the first number")

    if num1.lower() == "exit":
        print("Goodbye")
        break
    operator = input("Enter operator (+, -, *, /): ")
    num2 = input("Enter second number: ")

    try:
        num1 = float(num1)
        num2 = float(num2)
        result = calculator(num1, operator, num2)
        print("Answer:", result)
        
    except ValueError:
        print("Please enter valid numbers")
    
    finally:
        print()