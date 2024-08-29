from cs206draw import new_canvas,show

THE_SIZE = 256
LIMIT = 4

canvas = new_canvas(THE_SIZE + 1, THE_SIZE + 1, "gray")

def draw_space(xCenter, yCenter, boundingDim):
  side = boundingDim // 2
  
  if side >= LIMIT:
    left =   xCenter - side // 2
    top =    yCenter - side // 2
    right =  xCenter + side // 2
    bottom = yCenter + side // 2
    
    draw_space(left, top, side)
    draw_space(left, bottom, side)
    draw_space(right, top, side) 
    draw_space(right, bottom, side)
    
    canvas.rectangle((left+1, top+1, right, bottom), fill="white")
    show(100)

draw_space(THE_SIZE // 2, THE_SIZE // 2, THE_SIZE)
show()


