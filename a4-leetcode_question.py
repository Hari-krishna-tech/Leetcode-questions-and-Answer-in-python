"""
Find All Duplicates in an Array
------------------------------
Given an array of integers, 1 <= a[i] <= n (n = size of array) ,  <- trick is here
some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?
Example:
Input:
[4,3,2,7,8,2,3,1]
Output:
[2,3]
"""
#O(log(n)n) time but O(1) space with dictionary
#trivial solution
def duplicates(lst):
  lst.sort()
  repeated = []
  for i in range(len(lst)):
    if i < len(lst) -1:
      if lst[i] == lst[i+1]:
        repeated.append(lst[i])
  return repeated

print(duplicates([4,3,2,7,8,2,3,1]))
#need to find good solution 
# 1 <= a[i] <= n (n = size of array) ,  <- trick is here
def duplicates2(lst):
  repeated = []
  for i in range(len(lst)):
    index = abs(lst[i])-1
    if lst[index] < 0:
      repeated.append(abs(lst[i]))
    lst[index] = -lst[index]
  return repeated
print(duplicates2([4,3,2,7,8,2,3,1]))
"""
go to every value and make its value and make index =  value - 1
go to index and make it negative
if you found the index value already negative it is a duplicate
add that to duplicate array
Example
[4,3,2,7,8,2,3,1]
#go to 4
#make index = abs(4)-1 
#if lst[index = 3] < 0
#7 is not < 0 so don't add to duplicate array
#make 7 negative
#lst[index] = -lst[index]
#lst[3] = -lst[3]
7 = -7
now the list is [4,3,2,-7,8,2,3,1]
#go to 3
#make index = abs(3)- 1  //2
#check 2 is negative or not
#if negative add to repeated
#because we already seen it
#it's not so
#make 2 = -2
now the list is [4,3,-2,-7,8,2,3,1]
and go on like the 
return repeated list
think you understand the concept
"""