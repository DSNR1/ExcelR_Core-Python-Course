def myFunction():
    global a
    a = "LocalPythonObject"
    print("The value of a inside myFunction: ", a)


myFunction()
print("The value of a outside myFunction: ", a)