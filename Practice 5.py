runscored = 1

def localFunction():
    runscored = 2
    print("The value of runscored in localfunction(): ", runscored)


localFunction()
print("The value of runscored in main: ", runscored)