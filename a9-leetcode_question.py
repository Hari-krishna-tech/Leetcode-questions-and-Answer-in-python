"""
Median of Two Sorted Arrays
------------------------------
There are two sorted arrays nums1 and nums2 of size m and n
respectively.
Find the median of the two sorted arrays. The overall run time
complexity should be O(log (m+n)).
Example 1:
nums1 = [1, 3] 1,2,3
nums2 = [2]
The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4] 
The median is (2 + 3)/2 = 2.5
"""
import math
def median(arr1,arr2):
  if len(arr1) > len(arr2):
    return median(arr2,arr1)
  x = len(arr1)
  y = len(arr2) 
  low = 0
  high = len(arr1)
  while low <= high:
    partionX = ( high + low )//2
    partionY = ( x + y + 1 )//2 - partionX
    maxleftX  = arr1[partionX-1] if partionX != 0 else -math.inf
    maxleftY = arr2[partionY-1] if partionY != 0 else -math.inf

    minrightX = arr1[partionX] if partionX != x else math.inf
    minrightY = arr2[partionY] if partionY != y else math.inf
    if maxleftX <= minrightY and maxleftY <= minrightX:
      if (x+y)%2 == 0:
        return (max(maxleftX,maxleftY) + min(minrightY,minrightX))/2
      else:
        return max(maxleftX,maxleftY)
    elif maxleftX > minrightX:
      low -= 1 
    else:
      low += 1


print(median([1,2,3,4],[12,13,14,15]))
"""
Explanation
let's take two sorted Array
[1,2,3,4][12,13,14,15]
first we need to make sure arr1 is sorter or equal that's what i did in line:20
I found the mid(partionX) point of arr1 :(low+high)//2 (0+4)//2 = 2
my aim is to make two equal sides were if it is even or one side bigger than other by one
were one side is smaller one side is bigger
i need to seperate second array based one my above condition partionY
total len = x+y
and I add 1 for odd cases for little help you can avoid that
partionY =  (x+y+1)//2-partionX //(4+4+1)//2 - 2 = 4-2 = 2
so first time i choose 
partionX = 2
partionY = 2 


    maxleftX  = arr1[partionX-1] if partionX != 0 else -math.inf //if left is empty make it -infinity
    maxleftY = arr2[partionY-1] if partionY != 0 else -math.inf //if left is empty make it -infinity

    minrightX = arr1[partionX] if partionX != x else math.inf //if right is empty make it infinity
    minrightY = arr2[partionY] if partionY != y else math.inf //if right is empty make it infinity
1   2 | 3  4
12 13 | 14 15
if 2<14 and 13<4:
median = max(1,14) // because it is in the middle but it is not the case
elif 1<14:
  low -= 1//that is not the case here 
  we do -1 because our first arr value is higher we need to lessen it
                                          //if we do it
                                          partionX = (low+high)//2 = (-1+4)//2 =  1
                                          partionY = (x+y+1)//2 - partionX = 4-1 = 3
                                          1        |2 3 4
                                          12 13 14 |15
else:  
  low += 1 //we are going to do it now
  because leftX value is higher we need to lessen so we increase
partionX = (low+high)//2 = (1+4)//2 =  2
partionY = (x+y+1)//2 - partionX = 4-2 = 2
1  2 | 3 4
12 13| 14 15
there is no change now
so we again do the same thing in next loop
low += 1
partionX = (low+high)//2 = (2+4)//2 =  3
partionY = (x+y+1)//2 - partionX = 4-3 = 1

1  2  3 | 4
12      |13 14 15
//again we hit the same condition
low += 1
partionX = (low+high)//2 = (3+4)//2 =  3
partionY = (x+y+1)//2 - partionX = 4-3 = 1

1  2  3 | 4
12      |13 14 15
//we will hit the same condition
low += 1
partionX = (low+high)//2 = (4+4)//2 =  4
partionY = (x+y+1)//2 - partionX = 4-4 = 0
1 2 3 4 | {}   # infinity
{}      |12 13 14 15
#-infinity
now this
if 4 < 12 and -infinity < infinity:
  this condition satisfied
  8 is even
  median 4+12/2 = 8
#and  that's our solution in log(n+m) time by doing binary search

"""