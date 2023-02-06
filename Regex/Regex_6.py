import re

someString = '''Rohit made 122 runs, Virat made 96 runs, and Shubman made 126 and w
won the match.'''

# {"Rohit": 122, "Virat": 96, "Shubman": 126}

# 1. Create an object with Names as list, Pattern exists (Fisrt Letter caps)
# 2. Create an object storing all the scores, Patter is all numbers

lstNames = re.findall(r"[A-Z][a-z]+", someString)
#print(lstNames)
lstNums = re.findall(r"\d+", someString)
#print(lstNums)

#Approach 1
result = {}
for item in range(0, len(lstNames)):
    result[lstNames[item]] = lstNums[item]

print(result)


#Approach 2 using zip function
age = [36, 34, 22]

result = list(zip(lstNames, lstNums, age))
print("Zipping: ", result)