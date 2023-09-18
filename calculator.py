import math  # Import math module
import sys  # Import sys module


arg1 = sys.argv[1]   # Get first argument
operation = sys.argv[2]   # Get second argument
arg2 = sys.argv[3]  # Get operation

def calculate(arg1, arg2, operation):
    if operation in ["add", "+", "plus"]:
        try:
            return float(arg1) + float(arg2)
        except ValueError:
            return "Invalid input"
    elif operation in ["sub", "-", "minus"]:
        try:
            return float(arg1) - float(arg2)
        except ValueError:
            return "Invalid input"
    elif operation in ["mul", "*", "times"]:
        try:
            return float(arg1) * float(arg2)
        except ValueError:
            return "Invalid input"
    elif operation in ["div", "/", "divide"]:
        try:
            return float(arg1) / float(arg2)
        except ValueError:
            return "Invalid input"

print(calculate(arg1, arg2, operation))  # Print result