#
# Compute sine and cosine
#

import math

def sine(x):
  if -0.01 < x < 0.01:
        return x - (x**3 / 6)
    
    # Recursive case
  half_x = x / 2
  return 2 * sine(half_x) * cosine(half_x)

def cosine(x):
  if -0.01 < x < 0.01:
        return 1 - (x**2 / 2)
    
  # Recursive case
  half_x = x / 2
  return 1 - 2 * (sine(half_x))**2

def tabulate(a, b, step):
  print("%5s : %-10s %-10s %-10s %-10s" % ("x", "sine(x)", "cosine(x)",
                                      "math.sin(x)", "math.cos(x)"))
  for i in range(a, b+1):
    x = step * i
    print("%5g : %-10g %-10g %-10g %-10g" %
          (x, sine(x), cosine(x), math.sin(x), math.cos(x)))

if __name__ == "__main__":
  tabulate(-20, 20, 0.1)
