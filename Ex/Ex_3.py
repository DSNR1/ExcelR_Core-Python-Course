try:
    fh = open("ExceptionHandling.txt","w")
    fh.write("Opening the file.\n")
    userInput = input("Enter any number: ")
    result = 100/int(userInput)
    fh.write("The final result is {}\n".format(result))
    print(result)
    #fh.write("Closing the file \n")
    #fh.close()
except ValueError:
    print("Not a valid number, please enter numbers only")
except ZeroDivisionError:
    print("Please enter numbers greater than 0")
finally:
    fh.write("Closing the file \n")
    fh.close()