def get_num():
    num1 = int(input("Enter Num1 -> "))
    num2 = int(input("Enter Num2 -> "))


def add(num1, num2):
    print(num1, "+", num2, "=", num1 + num2)


def substract(num1, num2):
    print(num1, "-", num2, "=", num1 - num2)


def divide(num1, num2):
    print(num1, "/", num2, "=", num1 / num2)


def multiply(num1, num2):
    print(num1, "x", num2, "=", num1 * num2)


print("Hello World! Welcome to MyCalculator")
loop = 1
get_num()
while loop == 1:

    print("1 -> Addition")
    print("2 -> Subtraction")
    print("3 -> Multiplication")
    print("4 -> Division")
    print("5 -> Change Numbers")
    print("6 -> Exit")

    option = int(input("Enter the Option : "))

    if option == 0 or option > 0 and option == 6 or option < 6:
        print("\nValid input\n")
    else:
        print("Not Valid")

    if option == 1:
        add(num1=get_num(), num2=get_num())
