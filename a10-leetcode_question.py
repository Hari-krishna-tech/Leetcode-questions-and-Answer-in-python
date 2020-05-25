"""
K-th largest elenent in  an array 
Example:
[2,3,4,6,7] 2 
output:6
only k-th largest element on distinct
[1,2,3,4,6,6,5] 2
output: 6
"""
#trivial sort the array fing length - 1 - k th element
def k_th_largest_element1(arr,k):#O(nlog(n)) time 
  arr.sort()
  return arr[ len(arr) - k ]#O(1) space
#bad time complexity
print("least efficient but trivial O(nlog(n))")
print(k_th_largest_element1([1,2,3,4,6,6,5],2))
#print(k_th_largest_element1([2,3,4,6,7],3))

"""
Nice solution using Heap because finding maximum in heap is constant 

"""

#in heap pust O(log(n))
#we are pushing n element
#O(nlog(n))
#pop O(log(n))
# for k time we are doing it

# O((klog(n))
import heapq
def k_th_largest_element2(arr,k):
  heapq._heapify_max(arr) #O(n)
  for i in range(k):#O(klog(n))
    ans = heapq._heappop_max(arr)
  return ans

print("second best  O(klog(n))")
print(k_th_largest_element2([1,2,3,4,6,6,5],2))
#print(k_th_largest_element2([2,3,4,6,7],3))
#O(klog(n)) time
#O(1) space
#so we can just sort heaps are waste 
#no no no 
#we can a trick to bring in down to nlog(K)
#and O(k) extra  space
# let's see the magic below 

def k_th_largest_element3(arr,k):
  arr1 = []
  for i in range(k):
    heapq.heappush(arr1,arr[i])
  for i in range(k,len(arr)):
    if arr[i] > arr1[0]:
      heapq.heappop(arr1)
      heapq.heappush(arr1,arr[i])
  k_th_largest = heapq.heappop(arr1)
  return k_th_largest
print("best method  O(nlog(k))")    
print(k_th_largest_element3([1,2,3,4,4,5],3))

"""
own heap inplementation for fun
"""
class Max_Heap:
  def __init__(self):
    self.heap = []
    self.last_position = 0
  
  def push(self,element):
    if len(self.heap) == 0:
      self.heap.append(element)
    else:
      self.heap.append(element)
      self.last_position += 1
      self.trickle_up(self.last_position)
  def trickle_up(self ,last_pos):
    parent = (last_pos-1)//2
    if parent >= 0: 
      if self.heap[parent] < self.heap[last_pos]:
        self.swap(last_pos,parent) 
        self.trickle_up(parent)

  def swap(self,frm, to):
    tmp = self.heap[frm]
    self.heap[frm] = self.heap[to]
    self.heap[to] = tmp
  
  def pop(self):
    if len(self.heap) == 0:
      return
    data = self.heap[0]
    self.swap(0,self.last_position)
    self.last_position -= 1
    self.trickle_down(0)
    return data
  
  def trickle_down(self,pos):
    if pos <= self.last_position:
      left_child = pos * 2 + 1
      right_child = pos * 2 + 2
      if left_child <= self.last_position and right_child <= self.last_position:
        
        if self.heap[pos] < self.heap[left_child] and self.heap[left_child] > self.heap[right_child]:
          self.swap(pos,left_child)
          return self.trickle_down(left_child)
        elif self.heap[pos] < self.heap[right_child] and self.heap[left_child] < self.heap[right_child]:
          self.swap(pos,right_child)
          return self.trickle_down(right_child)
      elif right_child > self.last_position and left_child <= self.last_position:
        if self.heap[pos] < self.heap[left_child]:
          self.swap(pos,left_child)
          return self.trickle_down(left_child)
    
 
mh = Max_Heap()
mh.push(1)
mh.push(3)
mh.push(5)
mh.push(-1)
mh.push(10)
mh.push(11)
mh.push(9)
mh.push(8)
mh.push(-2)
print(mh.heap)
print(mh.last_position)
print(mh.pop())
print(mh.heap)
print(mh.last_position)
class Min_heap:
  def __init__(self):
    self.heap = []
    self.last_position = 0

  def heapify(self, arr):
    for i in arr:
      self.push(i)

  def push(self,element):
    if len(self.heap) == 0:
      self.heap.append(element)
    else:
      self.heap.append(element)
      self.last_position += 1
      self.trickle_up(self.last_position)
  def trickle_up(self ,last_pos):
    parent = (last_pos-1)//2
    if parent >= 0: 
      if self.heap[parent] > self.heap[last_pos]:
        self.swap(last_pos,parent) 
        self.trickle_up(parent)

  def swap(self,frm, to):
    tmp = self.heap[frm]
    self.heap[frm] = self.heap[to]
    self.heap[to] = tmp
  
  def pop(self):
    if len(self.heap) == 0:
      return
    data = self.heap[0]
    self.swap(0,self.last_position)
    self.last_position -= 1
    self.trickle_down(0)
    return data
  def peek(self):
    return self.heap[0]
  def trickle_down(self,pos):
    if pos <= self.last_position:
      left_child = pos * 2 + 1
      right_child = pos * 2 + 2
      if left_child <= self.last_position and right_child <= self.last_position:
        
        if self.heap[pos] > self.heap[left_child] and self.heap[left_child] < self.heap[right_child]:
          self.swap(pos,left_child)
          return self.trickle_down(left_child)
        elif self.heap[pos] > self.heap[right_child] and self.heap[left_child] > self.heap[right_child]:
          self.swap(pos,right_child)
          return self.trickle_down(right_child)
      elif right_child > self.last_position and left_child <= self.last_position:
        if self.heap[pos] > self.heap[left_child]:
          self.swap(pos,left_child)
          return self.trickle_down(left_child)

min_heap = Min_heap()
min_heap.push(-1)
min_heap.push(2)
min_heap.push(1)
min_heap.push(6)
min_heap.pop()
print(min_heap.heap)

def k_th_largest_element4(arr,k):
  heap = Min_heap()
  heap.heapify(arr[:k])
  for i in arr[k:]:
    if i > heap.peek():
      print(heap.heap)
      heap.push(i)
      heap.pop()
      print(heap.heap)
  return heap.peek()

print(k_th_largest_element4([2,4,6,2,5,8],2))

"""
my implementation doesn't work use library
"""
"""
 I found a better method than a heap 
 Quick select #O(n) Average
"""
def k_th_largest_element5(arr,k):
  low = 0
  high = len(arr) - 1
  return quickselect(arr,low,high,k)


def quickselect(arr,low,high,k):
  if low == high:
    return arr[low]
  pivotIndex = high
  pivotIndex = partition(arr,low ,high,pivotIndex)
  if k == pivotIndex:
    return arr[k]
  elif k < pivotIndex:
    pivotIndex -= 1
  else:
    pivotIndex += 1
  """it is hard"""

def partition(arr,low,high,pivotIndex):
  pass
      
