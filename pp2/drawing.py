from cs206draw import new_canvas,show

THE_SIZE = 512

canvas = new_canvas(THE_SIZE + 1, THE_SIZE + 1, "white")

# --------------------------------------------------------------------

def draw_front(x, y, side, level):
  if level < 1:
    return
  hs = side // 2
  left =   x - hs
  top =    y - hs
  right =  x + hs
  bottom = y + hs
  nside = int(side / 2.2)
  draw_front(left, top, nside, level-1)
  draw_front(left, bottom, nside, level-1)
  draw_front(right, top, nside, level-1) 
  draw_front(right, bottom, nside, level-1)
  canvas.rectangle((x-hs, y-hs, x+hs, y+hs), fill="gray", outline="black")
  
def draw_order(x, y, side, level):
  return 1
  raise NotImplementedError

def draw_right(x, y, side, level):
  return 1
  raise NotImplementedError

def draw_back(x, y, side, level):
  return 1
  raise NotImplementedError

# --------------------------------------------------------------------

if __name__ == "__main__":
  print("Click into the drawing or press <Enter> to see the next drawing")
  for level in range(1, 7):
    canvas.rectangle((0, 0, THE_SIZE, THE_SIZE), fill="white")
    draw_front(THE_SIZE // 2, THE_SIZE // 2, 5 * THE_SIZE // 9, level)
    show()

# --------------------------------------------------------------------
