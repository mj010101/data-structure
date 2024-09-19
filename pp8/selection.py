#
# select returns the k-th smallest element of a
#
def select(a, k):
  b = sorted(a)
  return b[k]

# Implement the function quick_select.
# It also returns the k-th smallest element of a.
def quick_select(a, k):
  if len(a) == 1:
      return a

  pivot = a[len(a) // 2]  # Pick pivot (e.g., middle element)

  # Partitioning into three lists
  smaller = [x for x in a if x < pivot]
  equal = [x for x in a if x == pivot]
  larger = [x for x in a if x > pivot]

  if k < len(smaller):
      # The k-th smallest is in the 'smaller' part
      return quick_select(smaller, k)
  elif k < len(smaller) + len(equal):
      # The k-th smallest is in the 'equal' part, so it's the pivot
      return pivot
  else:
      # The k-th smallest is in the 'larger' part
      return quick_select(larger, k - len(smaller) - len(equal))
  
  raise NotImplementedError

