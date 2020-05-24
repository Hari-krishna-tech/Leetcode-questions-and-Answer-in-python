"""
Reversing A LinkedList

"""
'''
simple Linked list implementation
'''
class Node:
  def __init__(self,data,next = None):
    self.data = data
    self.next = next


class LinkedList:
  def __init__(self):
    self.head = None
    self.length = 0
  
  def get_head(self):
    return self.head
  def add(self,data):
    node = Node(data)
    if self.head == None:
      self.head = node
      self.length += 1
    else:
      cur_node = self.head
      while cur_node.next != None:
        cur_node = cur_node.next
      cur_node.next = node 
      self.length += 1
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


ll = LinkedList()
# 9 5 6 6 3 3 5 5 5 5
ll.add(9)
ll.add(5)
ll.add(6)
ll.add(6)
ll.add(3)
ll.add(3)
ll.add(5)
ll.add(5)
ll.add(5)
ll.add(5)
print("before Reversing")
for i in ll:
  print(i)

print(ll.head.data)
# iterative method
def reverse(ll):
  pre_node = None
  cur_node = ll.head
  next = None

  while cur_node != None:
    next = cur_node.next
    cur_node.next = pre_node
    pre_node = cur_node
    cur_node = next
    

  ll.head = pre_node

reverse(ll)
print("after reversing")
for i in ll:
  print(i)

"""
recursive method
"""
def reverse_recursive(cur,pre):
  if cur.next is None:
    ll.head = cur
    cur.next = pre
    return

  next = cur.next
  cur.next = pre
  reverse_recursive(next, cur)

print("after reversing")
reverse_recursive(ll.get_head(),None)
for i in ll:
  print(i)