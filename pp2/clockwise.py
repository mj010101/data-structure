# Solve Towers of Hanoi with clockwise movements only

import sys

# --------------------------------------------------------------------

# Preconditions:
#   - n smallest disks are the top disks on pole source. // n
#   - destination is the pole after source in clockwise order // destination = source의 바로 오른쪽에 있는 pole
# Postcondition:
#   - n smallest disks are the top disks on pole destination.

def hanoi_cw(n, source, destination, spare):
  if n == 1:
    print("Move disk 1 from %s to %s" % (source, destination))
  else:
    # The following part is wrong (not using clockwise movements)!
    hanoi_cw(n-1, source, destination, spare)

    hanoi_cw(n-1, destination, spare, source)

    print("Move disk %d from %s to %s - test1" % (n, source, destination))

    hanoi_cw(n-1, spare, source, destination)

    hanoi_cw(n-1, source, destination, spare)
    
    
    

# --------------------------------------------------------------------

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Missing argument")
    sys.exit(1)
  n = int(sys.argv[1])
  hanoi_cw(n, 'A', 'B', 'C')

# --------------------------------------------------------------------
