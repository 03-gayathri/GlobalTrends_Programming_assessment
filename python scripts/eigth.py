''' code to create a Python function that takes two numbers and an operator (as a string) and 
performs the corresponding arithmetic operation (addition, subtraction, multiplication, or division).'''
import string
def calculate(num1:int, num2:int,operator:string):
    
    result = 0
    if operator == "+":
      result = num1 + num2
    elif operator == "-":
     if num1 > num2:
      result = num1 - num2
     else:
      result = num2 - num1
    elif operator == "*":
      result = num1 * num2
    elif operator == "/":
     if num2 == 0:
      print("Error! Division by zero is not possible")
     else:
      result = num1/num2
    else:
      print("Wrong input,program terminated")
    return result

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
operator = input("Enter any one of the operator (+,-,*,/): ")
print(calculate(num1,num2,operator))

