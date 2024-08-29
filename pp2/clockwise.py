# Solve Towers of Hanoi with clockwise movements only

import sys

# --------------------------------------------------------------------

# Preconditions:
#   - n smallest disks are the top disks on pole source.
#   - destination is the pole after source in clockwise order
# Postcondition:
#   - n smallest disks are the top disks on pole destination.

def hanoi_cw(n, source, destination, spare):
  if n == 1:
    print("Move disk 1 from %s to %s" % (source, destination))
  else:
    # The following part is wrong (not using clockwise movements)!
    hanoi_cw(n-1, source, spare, destination)
    print("Move disk %d from %s to %s" % (n, source, destination))
    hanoi_cw(n-1, spare, destination, source)

# --------------------------------------------------------------------

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Missing argument")
    sys.exit(1)
  n = int(sys.argv[1])
  hanoi_cw(n, 'A', 'B', 'C')

# --------------------------------------------------------------------
