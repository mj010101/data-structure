from cs206draw import new_canvas, show
import sys

THE_SIZE = 1024
LIMIT = 2

canvas = new_canvas(THE_SIZE + 1, THE_SIZE + 1, "white")

# plot an H, centered on (x, y) of the given side length
def drawH(x, y, size):
  # compute the coordinates of the 4 tips of the H
  x0 = x - size/2
  x1 = x + size/2
  y0 = y - size/2
  y1 = y + size/2
  
  # draw the 3 line segments of the H
  # left  vertical segment of the H
  canvas.line((x0, y0, x0, y1), fill="black")
  # right vertical segment of the H
  canvas.line((x1, y0, x1, y1), fill="black")
  # connect the two vertical segments of the H
  canvas.line((x0,  y, x1,  y), fill="black")
  show(100)

# plot an order n H-tree, centered on (x, y) of the given side length
def draw_tree(n, x, y, size):
  if (n == 0):
    return
  drawH(x, y, size)
  
  # compute x- and y-coordinates of the 4 half-size H-trees
  x0 = x - size/2
  x1 = x + size/2
  y0 = y - size/2
  y1 = y + size/2
  
  # recursively draw 4 half-size H-trees of order n-1
  # order can be rearranged
  draw_tree(n-1, x0, y0, size/2)    # lower left  H-tree
  draw_tree(n-1, x0, y1, size/2)    # upper left  H-tree
  draw_tree(n-1, x1, y0, size/2)    # lower right H-tree
  draw_tree(n-1, x1, y1, size/2)    # upper right H-tree

# read in a command line argument N and plot an order N H-tree
n = int(sys.argv[1])
draw_tree(n, THE_SIZE/2, THE_SIZE/2, THE_SIZE/2)
show()
