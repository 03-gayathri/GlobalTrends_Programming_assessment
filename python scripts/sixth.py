'''code to create a Python function that divides two numbers and handles the case where the 
divisor is zero by returning a custom error message.'''
def divide(num1:int, num2:int):
    try: 
        num3=num1/num2
        return num3
    except ZeroDivisionError: 
        return "Error: Division by zero is not possible."
num1=int(input("Enter dividend number:"))
num2=int(input("Enter divisor number:"))
print(divide(num1,num2))
