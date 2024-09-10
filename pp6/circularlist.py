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
    # 첫번째 노드를 생성하고, 그 노드가 스스로를 가리키도록 설정.
    node = Node(el)
    node.next = node
    node.prev = node
    self._front = node # 리스트의 시작 노드 (유일한 노드일 경우)
    return
    raise NotImplementedError
  
  def first(self):
    return self._front
    raise NotImplementedError

  def __repr__(self):
    # 리스트의 요소들을 문자열로 변환
    res = "["
    p = self._front
    # 원형 리스트를 순회하면서 각 요소를 문자열로 저장
    first_pass = True # self._front로 돌아오는 시작점. 처음 돌때만 True, 이후 부터 바로 false.
    while first_pass or p != self._front:
        first_pass = False
        res += str(p.el)
        p = p.next
        if p != self._front:
            res += ", "
    res += "]"
    return res
    raise NotImplementedError

  def remove(self, p):
    if p.next == p and p.prev == p:
      raise ValueError("Cannot remove only node of a CircularList")
    
    # p를 제거하고, 양옆의 노드(p.prev <> p.next)를 연결
    prev_node = p.prev
    next_node = p.next

    prev_node.next = next_node
    next_node.prev = prev_node

    # 삭제된 노드가 _front였다면, _front를 다음 노드로 업데이트
    if p == self._front:
      self._front = next_node
    
    return
    raise NotImplementedError

  def __len__(self):
    p = self._front
    count = 1
    current = p.next
    while current != self._front:
      count += 1
      current = current.next
    return count
    raise NotImplementedError

  def insert(self, p, el):
    new_node = Node(el)
    if len(self) == 0:
      self._front = new_node
      self._front.next = self._front
      self._front.prev = self._front
    else:
      prev_node = p.prev
      prev_node.next = new_node
      new_node.prev = prev_node
      new_node.next = p
      p.prev = new_node
    return
    raise NotImplementedError

  def append(self, x):
    # 리스트 마지막에 요소 추가 = 첫번째 노드 앞에 추가
    new_node = Node(x)
    if len(self) == 0:
      self._front = new_node
      self._front.next = self._front
      self._front.prev = self._front
    else:
      rear = self._front.prev
      rear.next = new_node
      new_node.prev = rear
      new_node.next = self._front
      self._front.prev = new_node
    return
    raise NotImplementedError
