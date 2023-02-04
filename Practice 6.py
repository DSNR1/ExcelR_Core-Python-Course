runscored = 1

def localFunction():
    runscored = 2
    print("The value of runscored in localfunction(): ", runscored)

def globalFunction():
    global runscored
    runscored = 3
    print("The value of runscored in globalFunction(): ", runscored)


print("The value of runscored in main: ", runscored)
localFunction()
globalFunction()