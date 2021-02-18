# This code subtracts the second number num2 from first number num1
# This code has a logic to check if num2 is smaller than num1 to give positive integer as an output

num1 = int(input('Enter the Number 1 '))
num2 = int(input('Enter the Number 2 '))
sub = num1 - num2
if num1 < num2:
    print("Enter Number 2 smaller than Number 1")
else:
    print("The value of",num1,"-" , num2,"is =", sub)