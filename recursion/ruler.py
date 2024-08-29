from cs206draw import new_canvas,show

THE_SIZE = 511

canvas = new_canvas(THE_SIZE + 1, 128, "white")

def draw_ruler(left, right, level):
  if level < 1:
    return
  mid = (left + right) // 2
  draw_ruler(mid + 1, right, level - 1)
  draw_ruler(left, mid - 1, level- 1)
  canvas.line((mid, 0, mid, 16 * level), fill=(0, 0, 128))
  #show(100)

draw_ruler(0, THE_SIZE - 1, 8)
show()
