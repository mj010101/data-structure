# Solve Towers of Hanoi

import sys

# Precondition: n smallest discs are the top discs on pole source.
# Postcondition: n smallest discs are the top discs on pole destination.
def solveHanoi(n, source, destination, spare):
  if n == 1:
    print("Move disc 1 from %s to %s" % (source, destination))
  else:
    solveHanoi(n-1, source, spare, destination)
    print("Move disc %d from %s to %s" % (n, source, destination))
    solveHanoi(n-1, spare, destination, source)

if len(sys.argv) != 2:
  print("Missing argument")
  sys.exit(1)

n = int(sys.argv[1])
solveHanoi(n, 'A', 'B', 'C')

