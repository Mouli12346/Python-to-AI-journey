#ERROR HANDELING
#Error handeling - with try and except

try:
    print(10/0)
except:
    print("cannot divide by 0")

print("program runs normally")

#handel different errors differntly
try:
    number = int(input("Enter a number:"))
    result = 100/number
    print("Result:", result)

except ValueError:
    print("please enter a valid number")
except ZeroDivisionError:
    print("cannot divide by zero")
except:
    print("something went wrong")

print("programme runs normally")

#Finally always runs no matter what error happens
try:
    number = int(input("Enter a number:"))
    result = 100/number
    print("Result:", result)

except ValueError:
    print("please enter a valid number")
except ZeroDivisionError:
    print("cannot divide by zero")
finally:
    print("Thank you for using calculator")
    print("No matter what the programme always runs")
    

