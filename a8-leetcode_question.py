"""
Longest Substring Without Repeating Characters
------------------------------
Given a string, find the length of the longest substring without
repeating characters.
Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that 
the answer must be a substring, "pwke" is a subsequence and not a
substring.
-------------
"""
def length_of_longest_sub_string(s):
  a_pointer = 0
  b_pointer = 0
  max_len = 0
  set_string = set()
  while b_pointer < len(s):
    if s[b_pointer] not in set_string:
      set_string.add(s[b_pointer])
      max_len = max(max_len,len(set_string))
      print(max_len)
      b_pointer += 1
    else:
      set_string.remove(s[a_pointer])
      a_pointer += 1
    print(set_string)
  return max_len

print(length_of_longest_sub_string("abcabcbb"))