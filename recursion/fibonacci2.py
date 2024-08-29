
def fib(n):
  F = [ 0, 1]
  for i in range(2, n+1):
    F.append(F[-1] + F[-2])
  return F[-1]
  
for i in range(1, 90):
  print("Fib(%d) = %d" % (i, fib(i)))

