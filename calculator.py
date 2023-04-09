
while True:
    try:
        print('Hello User, what is your name?')
        name = input()
        print('Ok ' + name + ' What two numbers will you use?')
        number1 = int(input("What is your first number?"))
        number2 = int(input("What is your second number?"))

        print('Well ' + name + ' What operation would you like to use?')
        operator = input('Enter an operator ( + - * /) ') #gathers operation user wants

        if operator == "+":
            print(number1 + number2)
        if operator == "-":
            print(number1 - number2)
        if operator == "*":
            print(number1 * number2)
        if operator == "/":
            print(number1 / number2)  
        break
            
    except ValueError:
        print("That is not a number try again.")


