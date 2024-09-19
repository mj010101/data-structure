#
# select returns the k-th smallest element of a
#
def select(a, k):
  b = sorted(a)
  return b[k]

# Implement the function quick_select.
# It also returns the k-th smallest element of a.
def quick_select(a, k):
  # 1. Base case와 Pivot을 설정한다.
  if len(a) <= 1:
    return a
  pivot = a[len(a) // 2]

  # 2. 리스트를 small/equal/large 세부분으로 나눈다. 
  # 리스트 컴프리헨션 (List comprehension)을 활용해서 조건별 리스트 생성.
  small = []
  equal = []
  large = []
  for item in a:
    if item < pivot:
      small.append(item)
    elif item == pivot:
       equal.append(item)
    else:
       large.append(item)
  # Alternative: List comprehension ver.
  # small = [x for x in a if x < pivot]
  # equal = [x for x in a if x == pivot]
  # large = [x for x in a if x > pivot]
  
  # k가 small 리스트의 길이보다 작으면 small 리스트에서 탐색 (ex. k = 5, len(small) = 6)
  if k < len(small):
      return quick_select(small, k)
  # k가 small + equal의 범위 내에 있으면, equal 리스트의 uniform한 값인 'pivot'을 리턴함.
  elif k < len(small) + len(equal):
      return pivot
  # k가 large 범위에 있으면 large 리스트에서 탐색
  # small과 equal에서 이미 a번째 b번째를 탐색했으니, large 리스트에서 k - (a+b) 번째를 구해야한다.
  # ex) a = [2, 4, 1, 8, 9, 5, 3], k = 5
  #     pivot = 4
  #     small = [2, 1, 3] // 3개 (k-3)
  #     equal = [4] // 1개 (k-1)
  #     large = [8, 9, 5] // Large에서 첫번째로 작은값을 찾으면 됨.
  else:
      return quick_select(large, k - len(small) - len(equal))
  
  raise NotImplementedError

