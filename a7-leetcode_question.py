"""
Add Two Numbers
------------------------------
You are given two non-empty linked lists representing two nonnegative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero,
except the number 0 itself.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
------------------------------
Explanation: 342 + 465 = 807.
"""
# LinkedList implementation added lot of extra things just for fun
class Node:
  def __init__(self,data,next=None):
    self.data = data
    self.next = next
  def __eq__(self,other):
    if isinstance(other,Node):
      if other.data == self.data:
        return True
    else:
      return False

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def get_tail(self):
    return self.tail
  
  def get_head(self):
    return self.head

  def get_length(self):
    return self.length

  def add_first(self,data):
    node = Node(data)
    self.length += 1
    if self.head == None:
      self.head = node
      self.tail = node   
    else:
      node.next = self.head
      self.head = node
      cur_node= self.head
      while cur_node.next != None:
        cur_node = cur_node.next
      self.tail = cur_node

  def add_last(self,data):
    node = Node(data)
    if self.head == None:
      self.add_first(data)
    else:
      self.tail.next = node
      self.tail = node
      self.length += 1
  
  def remove_first(self):
    if self.head == None:
      return 
    elif self.head.next == None:
      self.head = self.head.next
      self.tail=  self.head
      self.length -= 1
    else:
      self.head = self.head.next
      self.length -= 1
  
  def remove_last(self):
    if self.head == None and self.head.next == None:
      self.remove_first()
    else:
      cur_node=  self.head
      pre_node= None
      while cur_node.next != None:
        pre_node= cur_node
        cur_node = cur_node.next
      pre_node.next=  None
      self.tail = pre_node
      self.length -= 1
  
  def add(self ,data, pos):
    # 1 2 3 4 indexing
    if pos <= self.length:
      node = Node(data)
      if pos == 1:
        self.add_first(data)  
      else:
        cur_node=  self.head
        pre_node=  None
        i = 1
        while cur_node.next != None and i < pos:
          pre_node = cur_node
          cur_node = cur_node.next
          i += 1
        if cur_node.next == None:
          return self.add_last(data)
        node.next = cur_node
        pre_node.next = node
        self.length += 1
  def remove_by_position(self ,pos):
    if pos <= self.length:
      if pos == 1:
        return self.remove_last()
      else:
        cur_node = self.head
        pre_node=  None
        i =  1
        while i < pos:
          pre_node = cur_node
          cur_node = cur_node.next
          i += 1
        if cur_node.next == None:
          return self.remove_last()
        pre_node.next = cur_node.next
        self.length -= 1
  
  def remove_by_data(self,data):
    node = Node(data)
    if self.head != None:
      if self.head == node:
        return self.remove_first()
      else:
        cur_node = self.head
        pre_node = None
        while cur_node.next != None and cur_node != node:
          pre_node = cur_node
          cur_node = cur_node.next
        if cur_node == node:
          if cur_node.next == None:
            return self.remove_last()
          else:
            pre_node.next = cur_node.next
            self.length -= 1
    
  def append_list(self,head):
    size = 0
    cur_node = head
    while cur_node.next != None:
      cur_node = cur_node.next
      size += 1
    self.tail.next = head
    self.tail = cur_node
    self.length += size + 1
    

  def __iter__(self):
    self.cur_node = self.head
    return self

  def __next__(self):
    if self.cur_node == None:
      raise StopIteration
    else:
      data = self.cur_node.data
      self.cur_node = self.cur_node.next
      return data
"""END OF LINKED LIST"""
def sum_of_two(l1,l2):
  result1 = 0
  for i in l1:#O(m)
    result1 = (result1*10) + i
  result1 = reverse(result1)#O(n)

  result2 = 0
  for i in l2:#O(n)
    result2 = (result2*10) + i
  result2 = reverse(result2)#O(m)
  result = reverse(result1+result2)#O(m)
  print(result1,result2,result)
  ll = LinkedList()
  for i in str(result):#O(n)
    
    ll.add_last(int(i))
  return ll
def reverse(num):
  return int(str(num)[::-1])
#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8
l1 = LinkedList()
l1.add_last(2)
l1.add_last(4)
l1.add_last(3)
l2 = LinkedList()
l2.add_last(5)
l2.add_last(6)
l2.add_last(4)

result = sum_of_two(l1,l2)
for i in result:
  print(i)
#O(n) time O(n) space
#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8
def sum_of_two2(l1,l2):
  l3 = LinkedList()
  carry = 0
  while l1 != None or l2 != None:
    val1 = l1.data if l1 != None else 0
    val2 = l2.data if l2 != None else 0
    l3.add_last((val1+val2+carry)%10)
    carry = val1+val2//10
    l1 = l1.next
    l2 = l2.next
  return l3
#O(n) pretty neat solution I think
result1 = sum_of_two2(l1.get_head(),l2.get_head())
for i in result:
  print(i)

"""
        2->4->3
        5->6->4
        7->0->7+1 or 7->0->8
carry   0  1  0
"""