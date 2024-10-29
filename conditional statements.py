num=int(input("Enter a number: "))
if num%2==0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))

if num1>num2 and num1>num3:
    print(f"{num2} is the largest number.")
elif num2>num3 and num2>num3:
    print(f"{num2} is the largest number.")
else:
    print(f"{num3} is the largest number.")
