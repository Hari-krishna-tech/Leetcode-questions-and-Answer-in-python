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
"""
Let Palindrome = X * Y, both have n digits, and assume they are very close to 10^n
Denote X = 10^n - i, Y = 10^n - j, with assumption: i*j < 10^n
Palindrome = upper*10^n + lower = (10^n - i)*(10^n - j) = (10^n-i-j)*10^n + i*j
therefore: upper = 10^n-i-j, lower = i*j
Let a = i + j, then lower = i*(a-i), upper = 10^n-a
Algorithm: we iterate a and search for an integer i
i^2 - a*i + lower = 0 => (i-a/2)^2 = 0.25*a^2 - lower
Given a start from 2, check if sqrt(a^2 - lower*4) is an integer, then return upper*10^n + lower"""
def largest_palindrome_product_of_n_digit_no(n):
  if n == 1: return 9
  a = 2
  while a < 10**n:
    upper = 10**n-a
    lower = int(str(upper)[::-1])
    if a**2-lower*4 >= 0 and (a**2-lower*4)**0.5 == int((a**2-lower*4)**0.5):
      return (upper*10**n+lower) % 1337
    a += 1

print(largest_palindrome_product_of_n_digit_no(4))