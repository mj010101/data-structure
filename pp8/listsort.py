#
# DoublyLinkedList with Mergesort
#

class EmptyListError(Exception):
  pass

class Node:
  def __init__(self, el, next=None, prev=None):
    self.el = el
    self.next = next
    self.prev = prev

  def __repr__(self):
    return "<" + repr(self.el) + ">"

class DoublyLinkedList:
  def __init__(self, *els):
    self._front = Node(None)
    self._rear = Node(None, prev=self._front)
    self._front.next = self._rear
    for el in els:
      self.append(el)
  
  def is_empty(self):
    return self._front.next == self._rear

  def first(self):
    if self.is_empty():
      raise EmptyListError
    return self._front.next

  def last(self):
    if self.is_empty():
      raise EmptyListError
    return self._rear.prev

  def __repr__(self):
    res = "["
    p = self._front.next
    while p != self._rear:
      res += str(p.el)
      if p.next != self._rear:
        res += ", "
      p = p.next
    res += "]"
    return res

  def __len__(self):
    p = self._front.next
    count = 0
    while p != self._rear:
      count += 1
      p = p.next
    return count

  def insert_after(self, n, el):
    p = Node(el, n.next, n)
    n.next.prev = p
    n.next = p

  def prepend(self, el):
    # 가장 앞에 삽입
    self.insert_after(self._front, el)
  
  def append(self, el):
    # 가장 뒤에 삽입
    self.insert_after(self._rear.prev, el)

  def remove(self, n):
    n.prev.next = n.next
    n.next.prev = n.prev

# --------------------------------------------------------------------

  def median(self):
    "Returns the node in the middle of the list."
    front = self._front.next
    rear = self._rear.prev

    while front != rear and front.prev != rear:
      front = front.next
      rear = rear.prev
    # front를 반환하면 left-half가 아니라 right-half에서의 값을 반환함.

    return rear
    raise NotImplementedError

  def split(self, n):
    "Removes all nodes after n from this list and returns them in a new DoublyLinkedList object."
    new_list = DoublyLinkedList()

    # new_list의 첫 노드가 n 다음의 노드로 시작해야함.
    new_list._front.next = n.next
    n.next.prev = new_list._front

    # new_list의 마지막 노드는 self의 마지막 노드로 설정해야함.
    new_list._rear.prev = self._rear.prev
    self._rear.prev.next = new_list._rear

    # 원래 리스트를 n까지 잘라야 함.
    n.next = self._rear
    self._rear.prev = n

    return new_list
    raise NotImplementedError

  def steal(self, other):
    "Moves first node in other list to the end of this list."

    stolen_node = other.first()
    other.remove(stolen_node)

    # stolen_node의 값이 아니라, node 자체를 self 리스트의 끝에 추가.
    stolen_node.prev = self._rear.prev
    stolen_node.next = self._rear
    self._rear.prev.next = stolen_node
    self._rear.prev = stolen_node
    
    return
    raise NotImplementedError

  def merge(self, other):
    "Merges elements from sorted other list into this sorted list."
    left = self.split(self._front)  # move all elements to a new list
    # now merge left and other => into self! (Left에 빼놨다가, self로 다시 합치기.)
    left_node = left._front.next
    other_node = other._front.next

    # left 리스트와 other 리스트가 비어있을 때까지 반복.
    while left_node != left._rear or other_node != other._rear:
      # Case 1: Left가 비어있는 경우 
      # *(is_empty()를 활용하면 .el이 None 타입인 상황에서도 비교를 하기에 에러가 발생함.)
      if left_node == left._rear:
        self.append(other_node.el)
        other_node = other_node.next 
      # Case 2: Other가 비어있는 경우
      elif other_node == other._rear:
        self.append(left_node.el)
        left_node = left_node.next
      # Case 3: Left의 값이 더 작거나 같은 경우
      elif left_node.el <= other_node.el:
        self.append(left_node.el)
        left_node = left_node.next
      # Case 4: Other의 값이 더 작은 경우
      else:
        self.append(other_node.el)
        other_node = other_node.next
    
    # Other List를 비워줘야 함. [element를 기준으로 merge하기에, node가 남아있을 수 있음]
    other._front.next = other._rear
    other._rear.prev = other._front

    return
    raise NotImplementedError

# --------------------------------------------------------------------

  def sort(self):
    # is length <= 1 ?
    if self.is_empty() or self._front.next.next == self._rear:
      return
    other = self.split(self.median())
    self.sort()
    other.sort()
    self.merge(other)

# --------------------------------------------------------------------
