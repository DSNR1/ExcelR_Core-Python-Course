nums = range(1,11)
print("Numbers: ", list(nums))

sq = lambda n: n*n

# #Approach 1
result = []
for i in nums:
     result.append(sq(i))
 print("Squares: ",result)

#Approach 2
 result = [sq(i) for i in nums]
 print("Squares: ",result)

#Approach 3
# Using map
mobject = map(sq, nums)
sprint("List of sqaures of nums : ", list(mobject))
print("tuple of sqaures of nums : ", tuple(mobject))
