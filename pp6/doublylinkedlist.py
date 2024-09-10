
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
  def __init__(self):
    self._front = Node(None)
    self._rear = Node(None, prev=self._front)
    self._front.next = self._rear
  
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

  def find_first(self, x):
    p = self._front.next #p = 가장 앞에 있는 노드
    while p != self._rear:
        if p.el == x:
            return p
        p = p.next
    return None
    raise NotImplementedError

  def find_last(self, x):
    p = self._rear.prev
    while p != self._front:
      if p.el == x:
        return p
      p = p.prev
    return None
    raise NotImplementedError

  def count(self, x):
    p = self._front.next
    count = 0
    while p != self._rear:
      if p.el == x:
        count += 1
      p = p.next
    return count
    raise NotImplementedError

  def remove_first(self, x):
    p = self.find_first(x)
    if p:
      self.remove(p)
    return
    raise NotImplementedError

  def remove_last(self, x):
    p = self.find_last(x)
    if p:
      self.remove(p)
    return
    raise NotImplementedError

  def remove_all(self, x):
    p = self._front.next
    while p != self._rear:
      next_node = p.next # 현재 노드를 삭제하면 다음 노드를 접근할 수 없기 때문에 미리 저장
      if p.el == x:
        self.remove(p)
      p = next_node
    return self
    raise NotImplementedError

  def takeout(self, n, m):
    
    # 새로운 리스트를 생성하고, 잘라낸 부분의 앞뒤를 이어줌.
    new_list = DoublyLinkedList()
    new_list._front.next = n
    new_list._rear.prev = m
    n.prev.next = m.next
    m.next.prev = n.prev

    # n과 m의 앞뒤 링크를 수정하여 new_list가 독립적으로 동작하도록 만듦.
    n.prev = new_list._front
    m.next = new_list._rear

    return new_list
    raise NotImplementedError
