# Take a sequence of user inputs (numbers and comma seperated)
# Sum of those numbers
# Input: 1,2,3,4,5
# Output: 15

# Approach 2
UserInput = input(" Enter the sequence of numbers: ")
listnums = list(map(int, UserInput.split(",")))
print(sum(listnums))

# Approach 1
#UserInput = input(" Enter the sequence of numbers")
#print("UserInput")
#listnums = UserInput.split(",")

# result = 0
# for i in listnums:
#     result += int(i)
# print(result)