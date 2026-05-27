#Perrin
#Calculator
#initiate
#function
def Main():
    num1= int(input("Input the first number of your operation:"))
    operator= input("Please enter your chosen operator, ex. + - / *:")
    num2= int(input("Input the second numeber of your operation:"))
    if operator == "+":
       print(calc_sum(num1,num2))
    elif operator == "-":
        print(calc_sub(num1,num2))
    elif operator == "/":
        print(calc_div(num1,num2))
    elif operator == "*":
        print(calc_mult(num1,num2))
def calc_sum(x,y):
    z = x+y
    return z
def calc_sub(x,y):
    z=x-y
    return z
def calc_div(x,y):
    z=x/y
    return z
def calc_mult(x,y):
    z=x*y
    return z
#Main
Main()
