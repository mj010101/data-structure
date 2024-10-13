#
# Implementation of IMMUTABLE set using a Binary Search Tree
#

class _Node():
  def __init__(self, key, left=None, right=None):
    self.key = key
    self.left = left
    self.right = right

  def _description(self, level):
    ls = self.left._description(level+1) if self.left else ""
    rs = self.right._description(level+1) if self.right else ""
    return ls + str(self.key) + ("(%d) " % level) + rs

  def _find_first(self):
    "Return leftmost node in subtree." 
    p = self
    while p.left is not None:
      p = p.left
    return p

  def _find_last(self):
    "Return rightmost node in subtree." 
    p = self
    while p.right is not None:
      p = p.right
    return p

  def _find(self, key):
    "Return node with key key in this subtree, or None."
    if key == self.key:
      return self
    if key < self.key:
      return self.left._find(key) if self.left else None
    else:
      return self.right._find(key) if self.right else None

  def _insert(self, key):
    "Returns root of new subtree with key inserted."
    if key == self.key:
      return self
    elif key < self.key:
      if self.left is None:
        return _Node(self.key, _Node(key), self.right)
      nleft = self.left._insert(key)
      if nleft is self.left:
        return self
      return _Node(self.key, nleft, self.right)
    else:  # key > self.key
      if self.right is None:
        return _Node(self.key, self.left, _Node(key))
      nright = self.right._insert(key)
      if nright is self.right:
        return self
      return _Node(self.key, self.left, nright)

  def _remove_first(self):
    "Returns root of subtree with smallest key removed."
    if self.left is None:
      return self.right
    else:
      return _Node(self.key, self.left._remove_first(), self.right)

  def _remove(self, key):
    "Returns root of subtree with key key removed."
    if key < self.key and self.left is not None:
      nleft = self.left._remove(key)
      if nleft is self.left:
        return self
      else:
        return _Node(self.key, nleft, self.right)
    elif key > self.key and self.right is not None:
      nright = self.right._remove(key)
      if nright is self.right:
        return self
      else:
        return _Node(self.key, self.left, nright)
    elif key == self.key:
      if self.left is not None and self.right is not None:
        # Need to remove self, but has two children
        nkey = self.right._find_first().key
        return _Node(nkey, self.left, self.right._remove_first())
      else:
        # Need to remove self, which has zero or one child
        return self.left if self.left else self.right
    return self

  def _upper_neighbor(self, x):
    "Returns the smallest element of the subtree that is larger than x."
    current = self
    candidate = None  # 현재까지 찾은 upper neighbor 후보

    while current is not None:
        if current.key > x:
            candidate = current  # 현재 노드가 x보다 크면 upper neighbor 후보
            current = current.left  # 왼쪽 서브트리에서 더 작은 upper neighbor가 있는지 확인
        else:
            current = current.right  # x보다 크지 않다면 오른쪽 서브트리로 이동

    if candidate is None:
        raise KeyError(x)  # upper neighbor가 없을 경우 예외 발생

    return candidate.key
    raise NotImplementedError

  def _range(self, output, low, high):
    "Appends all elements of subtree in the range [low, high] to the output."
    if self is None:
        return  # 노드가 없으면 재귀 종료

    # 현재 노드가 범위의 하한보다 크면 왼쪽 서브트리를 탐색
    if self.left is not None and low < self.key:
        self.left._range(output, low, high)

    # 현재 노드가 범위 내에 있으면 출력 리스트에 추가
    if low <= self.key < high:
        output.append(self.key)

    # 현재 노드가 범위의 상한보다 작으면 오른쪽 서브트리를 탐색
    if self.right is not None and self.key < high:
        self.right._range(output, low, high)
    
    return
    raise NotImplementedError

  def _split(self, x):
    """Returns roots of two new trees, containing all elements of this subtree
that are <= x and > x, respectively."""
    if self.key <= x:
      # 현재 노드가 x보다 작거나 같은 경우, 왼쪽 서브트리는 그대로 유지하고
      # 오른쪽 서브트리를 분할하여 오른쪽에 해당하는 트리를 반환
      if self.right is None:
          return _Node(self.key, self.left, None), None  # 오른쪽에 더 이상 트리가 없음
      else:
          left_subtree, right_subtree = self.right._split(x)
          return _Node(self.key, self.left, left_subtree), right_subtree
    else:
        # 현재 노드가 x보다 큰 경우, 오른쪽 서브트리는 그대로 유지하고
        # 왼쪽 서브트리를 분할하여 왼쪽에 해당하는 트리를 반환
        if self.left is None:
            return None, _Node(self.key, None, self.right)  # 왼쪽에 더 이상 트리가 없음
        else:
            left_subtree, right_subtree = self.left._split(x)
            return left_subtree, _Node(self.key, right_subtree, self.right)
    raise NotImplementedError
    
# --------------------------------------------------------------------

class Set():
  def __init__(self):
    "Create an empty set."
    self._root = None

  def __repr__(self):
    return self._root._description(0) if self._root else "[]"

  def _find(self, key):
    return self._root._find(key) if self._root else None

  def is_empty(self):
    "Is this set empty?"
    return self._root is None

  def __contains__(self, key):
    return self._find(key) is not None
  
  def min(self):
    "Return smallest element in set." 
    return self._root._find_first().key if self._root else None

  def max(self):
    "Return largest element in set." 
    return self._root._find_last().key if self._root else None

  def __add__(self, key):
    "Return a new set containing all elements of this set plus key." 
    result = Set()
    if self._root is None:
      result._root = _Node(key)
    else:
      result._root = self._root._insert(key)
    return result

  def __sub__(self, key):
    "Return a new set containing all elements of this set except for key." 
    result = Set()
    if self._root is not None:
      result._root = self._root._remove(key)
    return result

  def upper_neighbor(self, x):
    "Returns the smallest element of the set that is larger than x."
    if self._root is None:
      raise KeyError(x)
    return self._root._upper_neighbor(x)
  
  def range(self, low, high):
    "Returns a sorted list of all elements x of the set with low <= x < high."
    output = []
    if self._root is not None:
      self._root._range(output, low, high)
    return output

  def split(self, x):
    "Returns pair of sets with all elements <= x and > x."
    left, right = Set(), Set()  # create output sets
    if self._root is not None:
      lroot, rroot = self._root._split(x)
      left._root = lroot
      right._root = rroot
    return left, right

# --------------------------------------------------------------------
