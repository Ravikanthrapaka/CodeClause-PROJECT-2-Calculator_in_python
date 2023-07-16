# #CODECLAUSE
# #PROJECT-2

# # CALCULATOR PROGRAM

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        print("Error: Division by zero")
        return None

def modulo(x, y):
    return x % y
    

def calculator():
    print("-------Welcome to Calculator program-----------")
    print("Operations:")
    print("1. Add")
    print("2. Subtract")   
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulo")
    print("6. Quit")
    print("-------------------")



    while True:
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = add(num1, num2)
            print("--------------")
            print("Result: ", result)
            print("--------------")
    
        elif choice == '2':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = subtract(num1, num2)
            print("--------------")
            print("Result: ", result)
            print("--------------")
        elif choice == '3':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = multiply(num1, num2)
            print("--------------")
            print("Result: ", result)
            print("--------------")
        elif choice == '4':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = divide(num1, num2)
            if result is not None:
                print("--------------")
                print("Result: ", result)
                print("--------------")

        elif choice == '5':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = modulo(num1, num2)
            print("--------------")
            print("Result: ", result)
            print("--------------")
        elif choice == '6':
            print("******Thank you for using the calculator!*****")
            break
        else:
            print("Invalid choice. Please try again.")

calculator()

