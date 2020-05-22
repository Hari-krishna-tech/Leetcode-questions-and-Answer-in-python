"""
Largest Palindrome Product
------------------------------
Find the largest palindrome made from the product of two n-digit
numbers.
 Since the result could be very large, you should return the largest
palindrome mod 1337.
Example:
Input: 2
Output: 987
Explanation: 99 x 91 = 9009, 9009 % 1337 = 987
Note:
The range of n is [1,8].
----------------------------"""
#first version pretty slow O(n^2) but works 
def Largest_palindrome_form_n_digit_no(n):
  if n == 1:return 9
  palindrome= []
  for i in range(10**n,10**(n-1),-1):
    for j in range(10**n,10**(n-1),-1):
      if is_palindrome(i * j):
        palindrome.append(i * j)
        
  return max(palindrome)%1337




def is_palindrome(integer):
  str_int=str(integer)
  return str_int == str_int[::-1]


print (Largest_palindrome_form_n_digit_no(2))
# good way