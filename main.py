import random

nums = [ ]
for i in range(0, 8):
    nums.append(random.randrange(0, 100))
    
print(nums)
#nums.sort()
#print(nums)

biggest = nums[0]
for i in range(0, 8):
    if nums[i]>biggest:
        biggest = nums[i]

print("The biggest number in the list is" ,  biggest)



