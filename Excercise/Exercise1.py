# Write a program which will find all such numbers which are divisible by 7 but not a multiple of 5
#Condition: numbers to be between 2000 and 3200 both to be included
#result should be in a comma seperated sequence in a single line

#nums = []
#for i in range(2000,3201):
#    if (i%7==0) and (i%5!=0):
#        nums.append(str(i))
#print(",".join(nums))


l=[str(i) for i in range(2000,3201) if i%7==0 and i%5!=0]
print(",".join(1))