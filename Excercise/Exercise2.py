## Write a Program where the out to a sequence of numbers is cubes in a dictionary
# seq: 2 to 20 both included
# output: {2:8, 3:27, ...} 

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
result = {}
for i in range(start, end+1):
    result[i] = i**3
print(result)    