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
    self.insert_after(self._front, el)
  
  def append(self, el):
    self.insert_after(self._rear.prev, el)

  def remove(self, n):
    n.prev.next = n.next
    n.next.prev = n.prev

# --------------------------------------------------------------------

  def median(self):
    "Returns the node in the middle of the list."
    raise NotImplementedError

  def split(self, n):
    "Removes all nodes after n from this list and returns them in a new DoublyLinkedList object."
    raise NotImplementedError

  def steal(self, other):
    "Moves first node in other list to the end of this list."
    raise NotImplementedError

  def merge(self, other):
    "Merges elements from sorted other list into this sorted list."
    left = self.split(self._front)  # move all elements to a new list
    # now merge left and other
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
