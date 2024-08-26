import math

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
        return "don't divide(Infinite)"
def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "diobidience number"
def power(x, y):
    return x ** y
def factorial(x):
    if x >= 0:
        return math.factorial(x)
    else:
        return "diobidience number"
def logarithm(x, base):
    if x > 0 and base > 0 and base != 1:
        return math.log(x, base)
    else:
        return "diobidience number"

print("WELCOME..!!! SIMPLE SCIENTIFIC CALCULATOR... :)")
print("select anyone:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Maltiplication (*)")
print("4. Division (/)")
print("5. Square root (√)")
print("6. Power 0")
print("7. Factorial (!)")
print("8. Logaridom")
print("0. Cancel")

while True:
    choice = input("select anyone (0-8): ")

    if choice == '0':
        print("off calculator...")
        break

    elif choice in ['1', '2', '3', '4', '6']:
        try:
            num1 = float(input("enter the first number: "))
            num2 = float(input("enter the second number: "))

            if choice == '1':
                print("addition result: ", add(num1, num2))

            elif choice == '2':
                print("subtraction result: ", subtract(num1, num2))

            elif choice == '3':
                print("maltiplication result: ", multiply(num1, num2))

            elif choice == '4':
                print("division result: ", divide(num1, num2))

            elif choice == '6':
                print("power result: ", power(num1, num2))
        except ValueError:
            print("Invaild number. Enter the number correctly")


    elif choice in ['5', '7']:
        try:
            num = float(input("write number: "))

            if choice == '5':
                print("square_root's result: ", square_root(num))

            elif choice == '7':
                print("factorial's result: ", factorial(int(num)))

        except ValueError:
            print("I apologize for the incomplete response. Here's the continuation of the code: ")

            print("Invaild number. Enter the number correctly")

    elif choice == '8':
        try:
            num = float(input("write number: "))
            base = float(input("write logaridom container: "))

            print("logarithm's result: ", logarithm(num, base))

        except ValueError:
            print("Invaild number. Enter the number correctly")

    else:
        print("Invaild number. Enter the number correctly")