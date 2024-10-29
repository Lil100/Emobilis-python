# create a program that checks a student performance
marks=int(input("Enter your marks: "))

if 100 >= marks >=90:
    print("You have an A")
elif 79 >= marks >=60:
    print("You have an B")
elif marks<=59 and marks>=40:
    print("You have an C")
elif marks>=39 and marks>=0:
    print("You have failed")
else:
    print("Invalid marks")