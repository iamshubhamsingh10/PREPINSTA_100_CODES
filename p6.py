#greatest of 3 numbers
num1=int(input("Enter the number"))
num2=int(input("Enter the number"))
num3=int(input('Enter the number'))
if num1>num2 and num1>num3:
    print("Number 1 is greater",num1)
elif num2>num1 and num2>num3:
    print("Number 2 is greater",num2)
else:
    print("Number 3 is the greatest")