"""
Two Sum
------------------------------
Given an array of integers, return indices of the two numbers such
that they add up to a specific target.
You may assume that each input would have exactly one solution, and
you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
#make use of our  hash table
def sum_of_two(nums, target):
  nums_dict = {}
  index = 0
  for i in nums:
    nums_dict[i] = index
    index += 1
  if nums_dict[2]:
    print("zero is not false")
  
  for i in range(len(nums)):
    complement = target - nums[i]
    if complement in nums_dict:
      return list((i,nums_dict[complement]))
    
#O(n) space
#O(n) time

print(sum_of_two([2, 6, 7, 15,0],10))