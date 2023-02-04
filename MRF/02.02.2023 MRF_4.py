from functools import reduce
nums = range (1, 11)
myFunc = lambda x, y: x * y
#print(myFunc (7,8))
print("Nums :", nums)
result = reduce(myFunc,nums)
print("Result: ", result)