"""
Given a sorted array consisting of only integers where every element
appears twice except for one element which appears once. Find this
single element that appears only once.
Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10
Note:
Your solution should run in O(log n) time and O(1) space.

"""
def find_single_element_in_sorted_array(sorted_arr,low,high):
  if low == high:
    return sorted_arr[low]
  mid =  low + (high-low)//2
  if mid % 2 != 0:
    if sorted_arr[mid] == sorted_arr[mid-1]:
      return find_single_element_in_sorted_array(sorted_arr,mid+1,high)
    return find_single_element_in_sorted_array(sorted_arr,low,mid)
  else:
    if sorted_arr[mid] == sorted_arr[mid+1]:
      return find_single_element_in_sorted_array(sorted_arr,mid+2,high)
    return find_single_element_in_sorted_array(sorted_arr,low,mid);

print(find_single_element_in_sorted_array([1,1,2,2,3,3,4,4,5,5,6,6,7,7,8],0,14))
