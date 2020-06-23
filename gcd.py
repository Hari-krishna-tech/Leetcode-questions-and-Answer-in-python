#Euclidean Algorithm method 1 best O(log(N))
def gcd(num1,num2):
  print(num1,num2)
  if num1 == 0:
    return num2
  return gcd(num2%num1,num1)
print(gcd(36,60))
#Euclidean Algorithm method 2
def gcd2(num1,num2):
  print(num1,num2)
  # 0 is divided by everything except 0
  if num1 == 0:
    return num2
  if num2 == 0:
    return num1
  if num1 > num2:
    return gcd2(num1-num2,num2)
  return gcd2(num1,num2-num1)
print(gcd2(36,60))