import sys
from doublylinkedlist import DoublyLinkedList

def josephus(n, m):
  L = DoublyLinkedList()
  for i in range(1, n+1):
    L.append(chr(ord('A') + i - 1))
  p = L.first()
  for i in range(n-1):
    print(L, p.el)
    for j in range(m):
      p = p.next
      if p.el is None:
        p = L.first()
    q = p
    p = p.next
    if p.el is None:
      p = L.first()
    L.remove(q)
  return L.first().el

result = josephus(int(sys.argv[1]), int(sys.argv[2]))
print("The last one is ", result)
