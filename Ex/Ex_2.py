try:
    userInput = input("Enter any number: ")
    result = 100/int(userInput)
    print(result)
except ValueError:
    print("Not a valid number, please enter numbers only")
except ZeroDivisionError:
    print("Please enter numbers greater than 0")