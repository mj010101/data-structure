#
# Implementation of dict using a Binary Search Tree
#  WITHOUT recursion for insertion and deletion
#

class _Node():
  def __init__(self, key, value, left=None, right=None):
    self.key = key
    self.value = value
    self.left = left
    self.right = right

  # This method is still recursive
  # We will only use it for small trees to test your methods
  def _description(self, level):
    ls = self.left._description(level+1) if self.left else ""
    rs = self.right._description(level+1) if self.right else ""
    return ls + str(self.key) + ("(%d) " % level) + rs

  def _find_first(self):
    p = self
    while p.left is not None:
      p = p.left
    return p

  def _find_last(self):
    p = self
    while p.right is not None:
      p = p.right
    return p

  def _find(self, key):
    raise NotImplementedError

  def _insert(self, key, value):
    raise NotImplementedError

  # Remove node with smallest key in the subtree rooted at this node
  # Returns the new root.
  def _remove_first(self):
    raise NotImplementedError

  # Returns the new root.
  def _remove(self, key):
    raise NotImplementedError

# --------------------------------------------------------------------

class dict():
  def __init__(self):
    self._root = None

  def __str__(self):
    return self._root._description(0) if self._root else "[]"

  def _find(self, key):
    return self._root._find(key) if self._root else None

  def __getitem__(self, key):
    n = self._find(key)
    if n is None:
      raise KeyError(key)
    return n.value 

  def get(self, key, v = None):
    n = self._find(key)
    return n.value if n else v

  def __contains__(self, key):
    return self._find(key) is not None

  def __setitem__(self, key, value):
    if self._root is None:
      self._root = _Node(key, value)
    else:
      self._root._insert(key, value)

  def firstkey(self):
    return self._root._find_first().key if self._root else None

  def lastkey(self):
    return self._root._find_last().key if self._root else None

  def __delitem__(self, key):
    if self._root:
      self._root = self._root._remove(key)

# --------------------------------------------------------------------
