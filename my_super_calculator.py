#My super calculator

#We create 4 functions for 4 types of operations :

def addition(x,y):
    return x + y

def substraction(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division(x,y):
    return x / y

print("""Hi, welcome to my super calculator \n
        1- Addition\n
        2- Substraction\n
        3- Multiplication\n
        4- Division\n""")

#while loop with boolean

while True :
    choice = input("Choose a type of operation\n")

    if choice in ('1','2','3','4') :
        num1 = int(input("Enter your first number :"))
        num2 = int(input("Enter your second number :"))

        if choice == '1' :
            print (num1 , "+", num2, "=", addition(num1, num2))

        if choice == '2' :
            print (num1 , "-", num2, "=", substraction(num1, num2))
            
        if choice == '3' :
            print (num1 , "*", num2, "=", multiplication(num1, num2))

        if choice == '4' :
            print (num1 , "/", num2, "=", division(num1, num2))

        other_choice = input("Do you want to have another operation ?")
        if other_choice == "no" :
            break


#Without math import library