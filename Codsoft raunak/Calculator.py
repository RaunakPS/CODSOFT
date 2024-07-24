# Define a function for each arithmetic operation  
def add(x, y):  
  return x + y  
  
def sub(x, y):  
  return x - y  
  
def mul(x, y):  
  return x * y  
  
def div(x, y):  
  if y == 0:
      raise ValueError("Cannot divide by zero!")
      return x/y  
  
# Prompt the user to input two numbers and an operation choice  
num1 = float(input("Enter the first number: "))  
num2 = float(input("Enter the second number: "))  
operation = input("Enter the operation (+, -, *, /): ")  
  
# Perform the calculation based on the operation choice  
if operation == "+":  
  result = add(num1, num2)  
elif operation == "-":  
  result = sub(num1, num2)  
elif operation == "*":  
  result = mul(num1, num2)  
elif operation == "/":  
  result = div(num1, num2)  
else:  
  raise ValueError("Invalid operation!")  
  
# Display the result  
print("Result:",result)
