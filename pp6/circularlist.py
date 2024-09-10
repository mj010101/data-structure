#
# A circular doubly-linked list
#

class Node:
  def __init__(self, el, next=None, prev=None):
    self.el = el
    self.next = next
    self.prev = prev

  def __repr__(self):
    return "<" + repr(self.el) + ">"

class CircularList:
  def __init__(self, el):
    raise NotImplementedError
  
  def first(self):
    raise NotImplementedError

  def __repr__(self):
    res = "["
    raise NotImplementedError
    res += "]"
    return res

  def remove(self, p):
    raise NotImplementedError

  def __len__(self):
    raise NotImplementedError

  def insert(self, p, el):
    raise NotImplementedError

  def append(self, x):
    raise NotImplementedError
