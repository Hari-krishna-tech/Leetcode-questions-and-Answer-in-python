"""
merge point of two linked list
"""
# LinkedList implementation added lot of extra things JFF
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

common = LinkedList()
common.add_first(-10)
common.add_first(-9)
common.add_first(-8)
common.add_first(-7)
common.add_first(-6)




ll1 = LinkedList()
ll1.add_first(1) 
ll1.add_first(2)
ll1.add_first(3)
ll1.add_first(4)
ll1.add_first(5)
ll1.add_last(6)
ll1.add(10,3)
ll1.add(-1,1)
#ll1.remove_first()
#ll1.remove_last()
ll1.remove_by_position(3)
ll1.remove_by_position(3)
ll1.remove_by_data(1)
ll1.remove_by_data(2)
ll1.remove_by_data(5)
ll1.append_list(common.get_head())
for i in ll1:
  print(i)
print("length: ",ll1.get_length())
print("head: ",ll1.get_head().data)
print("tail: ",ll1.get_tail().data)
    
ll2 = LinkedList()
ll2.add_first(1)
ll2.add_first(2)
ll2.add_first(3)
ll2.add_first(4)
ll2.add_first(5)
ll2.add_first(6)
ll2.append_list(common.get_head())


for i in ll2:
  print(i)
print("length: ",ll2.get_length())
print("head: ",ll2.get_head().data)
print("tail: ",ll2.get_tail().data)
    
"""
Actuall point 
"""
