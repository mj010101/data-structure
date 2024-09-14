#
# Implementation of a sparse matrix
#

class Node(object):
  """Objects of type Node represent all non-zero entries of the matrix.
A Node object stores the coordinates of the entry, its value el,
and has a link to the next non-zero entry to the right (in the same row)
and below (in the same column)."""
  def __init__(self, row, col, el, right, down):
    self.row = row
    self.col = col
    self.el = el
    self.right = right
    self.down = down

class Matrix(object):
  def __init__(self, nrows, ncols):
    self.nrows = nrows
    self.ncols = ncols
    self._prow = [None] * nrows
    self._pcol = [None] * ncols

  def _findnode(self, row, col):
    """Returns the node for (row, col) and the previous node in the same row.
Both are None if they do not exist."""
    p = self._prow[row]
    q = None
    while p is not None and p.col < col:
      q = p
      p = p.right
    if p is None or p.col == col:
      return p, q
    return None, q

  def _insertnode(self, row, col, q, el):
    """Insert a new node for entry (row, col) with value el.
q is the previous node on the same row, or None."""
    n = Node(row, col, el, None, None)

    # 1. el이 0이면 삽입하지 않음. 해당 basecase가 없으면 무분별하게 node를 생성하여 에러가 뜸.
    if el == 0:
      return
    # 2. q가 None이면, n을 가장 처음에 삽입. q가 존재한다면, q 직후에 삽입.
    if q is None:
      n.right = self._prow[row]
      self._prow[row] = n
    else:
      n.right = q.right
      q.right = n
    
    #2. Column에서도 row와 마찬가지로 삽입.
    # p = self._pcol[col]
    # if p is None or p.row > row: # 첫번째 열이거나 삽입할 위치가 첫 노드보다 앞일경우.
    #   n.down = self._pcol[col]
    #   self._pcol[col] = n
    # else:
    #   n.down = p.down
    #   p.down = n
    p = self._pcol[col]
    prev_col_node = None

    while p is not None and p.row < row:
        prev_col_node = p
        p = p.down

    if prev_col_node is None:
        # 열의 첫 번째 노드로 삽입
        n.down = self._pcol[col]
        self._pcol[col] = n
    else:
        # 열의 중간 또는 끝에 삽입
        n.down = prev_col_node.down
        prev_col_node.down = n
    
    return  
    raise NotImplementedError

  def _removenode(self, p, q):
    "Remove the node p. q is the previous node on the same row, or None."
    # 1. Row 방향에서의 노드 삭제
    if q is None:
      self._prow[p.row] = p.right
    else:
      q.right = p.right
    # 2. Column 방향에서의 노드 삭제
    prev_col_node = None
    current_col_node = self._pcol[p.col]
    
    while current_col_node is not None and current_col_node != p:
      prev_col_node = current_col_node
      current_col_node = current_col_node.down
    if prev_col_node is None:
      self._pcol[p.col] = p.down
    else:
      prev_col_node.down = p.down

    return
    raise NotImplementedError

  def __getitem__(self, pos):
    "Return matrix entry pos = (row, col)."
    row, col = pos
    p, q = self._findnode(row, col)
    if p is None:
      return 0.0
    return p.el

  def __setitem__(self, pos, el):
    "Set matrix entry pos = (row, col) to value el."
    row, col = pos
    p, q = self._findnode(row, col)
    if p is None:
      if el != 0.0:
        self._insertnode(row, col, q, el)
    else:
      if el == 0.0:
        self._removenode(p, q)
      else:
        p.el = el
    
  def __repr__(self):
    s = ""
    for row in range(min(self.nrows, 10)):
      if row == 0:
        s += "/"
      elif row == self.nrows-1:
        s += "\\"
      else:
        s += "|"
      for col in range(min(self.ncols, 10)):
        s += "%6s " % self[row, col]
      if self.ncols > 10:
        s += "... "
      if row == 0:
        s += "\\\n"
      elif row == self.nrows-1:
        s += "/\n"
      else:
        s += "|\n"
    if self.nrows > 10:
      s += "...\n"
    return s

  def __eq__(self, rhs):
    "Test two matrices for equality."
    if self.nrows != rhs.nrows or self.ncols != rhs.ncols:
      return False
    for row in range(self.nrows):
      p1 = self._prow[row]
      p2 = rhs._prow[row]
      while p1 is not None and p2 is not None:
        if p1.col != p2.col or p1.el != p2.el:
          return False
        p1 = p1.right
        p2 = p2.right
      if p1 is not None or p2 is not None:
        return False
    return True

  def __mul__(self, rhs):
    "Multiply matrix with vector from the right."
    if self.ncols != len(rhs):
      raise ValueError("Dimensions of matrix and vector do not match")
    result = [0.0] * self.nrows

    for i in range(self.nrows):
      node = self._prow[i]
      while node:
        result[i] += node.el * rhs[node.col]
        node = node.right
    return result
    raise NotImplementedError

  def __rmul__(self, lhs):
    "Multiply matrix with vector from the left."
    if self.nrows != len(lhs):
      raise ValueError("Dimensions of matrix and vector do not match")
    result = [0.0] * self.ncols

    for j in range(self.ncols):
      node = self._pcol[j]
      while node:
        result[j] += lhs[node.row] * node.el
        node = node.down
    return result
    raise NotImplementedError

  def transposed(self):
    result = Matrix(self.ncols, self.nrows)

    for i in range(self.nrows):
      node = self._prow[i]
      while node:
        p, q = result._findnode(node.col, node.row)
        result._insertnode(node.col, node.row, q, node.el) #next node인 q를 명시해줘야 값을 누락하지 않고 제대로 transpose 됨.
        node = node.right
    return result
    raise NotImplementedError

  def __add__(self, rhs):
    if self.nrows != rhs.nrows or self.ncols != rhs.ncols:
      raise ValueError("Dimensions of matrices do not match")
    result = Matrix(self.nrows, self.ncols)

    # 각 row의 노드를 확인
    for i in range(self.nrows):
      p_self = self._prow[i]
      p_rhs = rhs._prow[i]

      while p_self or p_rhs:
        # case 1: self에만 값이 있을 때
        if p_self and (not p_rhs or p_self.col < p_rhs.col):
          result [i, p_self.col] = p_self.el
          p_self = p_self.right
        # case 2: rhs에만 값이 있을 때
        elif p_rhs and (not p_self or p_rhs.col < p_self.col):
          result[i, p_rhs.col] = p_rhs.el
          p_rhs = p_rhs.right
        # case 3: 두 matrix에 모두 값이 존재할 때
        else:
          result[i, p_self.col] = p_self.el + p_rhs.el
          p_self = p_self.right
          p_rhs = p_rhs.right
      
    return result
    raise NotImplementedError

# --------------------------------------------------------------------

def identity(n):
  "Create an nxn identity matrix."
  M = Matrix(n, n)
  for i in range(n):
    M[i,i] = 1.0
  return M

# --------------------------------------------------------------------

if __name__ == "__main__":
  m = identity(4)
  print(m)
  m[1,1] = 7
  print(m)
  m[2,1] = 13
  print(m)
  m[0,3] = -2
  print(m)
  m[3,3] = 0
  print(m)
  m[0,0] = 0
  m2 = Matrix(4, 4)
  m2[0,3] = -2
  m2[1,1] = 7
  m2[2,1] = 13
  print(m2)
  print(m == m2)
  m2[2,2] = 1
  print(m == m2)
  print(m * [ 1, 2, 3, 4 ] )
  print([1, 2, 3, 4] * m)
  # Test
  print("***********")
  print(m)
  print("***********")
  # Test
  t = m.transposed()
  print(t)
  print([1, 2, 3, 4] * t)
  print(t * [ 1, 2, 3, 4 ] )
  m3 = m + t
  print(m3)
  print(m3 == m3.transposed())
  
# --------------------------------------------------------------------
