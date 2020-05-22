"""
Find All Duplicates in an Array
------------------------------
Given an array of integers, 1 &le; a[i] &le; n (n = size of array),
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