
def fib(n):
  if n == 1:
    return (0, 1)
  else:
    a, b = fib(n-1)
    return (b, a+b)
  
for i in range(1, 90):
  print("Fib(%d) = %d" % (i, fib(i)[1]))



