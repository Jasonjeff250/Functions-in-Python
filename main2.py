#a simple calculator using functions
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):  
    return a*b
def divide(a,b):
    return a/b
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
print("Select your operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
user_input=int(input("Enter your choice:"))
if user_input==1:
    result=add(num1,num2)
    print("Result:",result)
elif user_input==2:
    result=subtract(num1,num2)
    print("Result:",result)
elif user_input==3:
    result=multiply(num1,num2)
    print("Result:",result)
elif user_input==4:
    result=divide(num1,num2)
    print("Result:",result)