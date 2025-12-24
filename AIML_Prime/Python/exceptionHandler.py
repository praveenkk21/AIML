x=5
try:
    y=10/int(x)
    print("result is:",y)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("Execution completed.")