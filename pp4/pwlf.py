#
# A class representing a piecewise linear function
#
# --------------------------------------------------------------------

class PieceWiseLinear(object):
  """A piecewise linear function"""
  def __init__(self, x0, y0, x1, y1):
    if x1 <= x0:
      raise ValueError("x1 must be larger than x0")
    self.x0 = x0
    self.y0 = y0
    self.x1 = x1
    self.y1 = y1

    self.segments = [(x0, y0, x1, y1)]
    return
    raise NotImplementedError

  def domain(self):
    """Return domain interval as a pair."""
    return (self.segments[0][0], self.segments[-1][2])
    raise NotImplementedError
                          
  def __str__(self):
    # WARNING: Would incur error for .join case.
    # 방안 idea: initial point, intersecting point, final point를 리스트에 담는다.
    #           이후, 중복되지 않게 (%g, %g)로 출력한다. 
    segment_strs = []
    for i, (x0, y0, x1, y1) in enumerate(self.segments):
        # Append the starting point only once
        if i==0:
            segment_strs.append("(%g, %g)" % (x0, y0))
        # Append the ending point of the current segment
        segment_strs.append("(%g, %g)" % (x1, y1))
    result = segment_strs
    return "..".join(result)
    raise NotImplementedError

  def __call__(self, x):
    """Evaluate this function at x-coordinate x."""
    d = self.domain()
    if x < d[0] or x > d[1]:
      raise ValueError("argument is not in domain")
    # f.segment = [(1, -1, 3, 1), (3, 1, 7, -5)]
    #           = [(x_1, y_1, x_2, y_2), (x_2, y_2, x_3, y_3)]
    global value
    for (x0, y0, x1, y1) in self.segments:
        if x0 <= x <= x1:  # Check if x is within this segment
            slope = (y1 - y0) / (x1 - x0)
            value = slope * (x - x0) + y0
    return value
    raise NotImplementedError

  def join(self, rhs):
    """Join two piecewise linear functions."""
    # d1: (self.x0, self.x1) | d2: (rhs.x0, rhs.x1)
    # Condition 1) self.x1 == rhs.x0
    # Condition 2) self.y1 == rhs.y1
    # 짜야 하는 코드
    # i) self.x0 =< x =< self.x1 => return self(x)
    # ii) self.x1 =< x =< rhs.x1 => return rhs(x)

    new_function = PieceWiseLinear(self.segments[0][0], self.segments[0][1], self.segments[0][2], self.segments[0][3])
    
    # Add all segments from rhs
    for seg in rhs.segments:
        new_function.segments.append(seg)
    
    return new_function
    raise NotImplementedError

  def __rmul__(self, lhs):
    """Multiplication of a number lhs with a piecewise linear function.
Returns a new function, this function remains unchanged."""
    new_segments = [
        (x0, y0 * lhs, x1, y1 * lhs)
        for (x0, y0, x1, y1) in self.segments
    ]
    
    # Create a new PieceWiseLinear object
    new_pwlf = PieceWiseLinear(self.x0, self.y0 * lhs, self.x1, self.y1 * lhs)
    new_pwlf.segments = new_segments
    return new_pwlf
  
    raise NotImplementedError

  def add_pwlf(self, rhs, factor):
    """Returns the sum of this function and factor * rhs,
where rhs is another piecewise linear function.
The domain of the result is the intersection of the two domains.
Returns a new function, this function remains unchanged."""
    x0a, x1a = self.domain()
    x0b, x1b = rhs.domain()
    x0 = max(x0a, x0b)
    x1 = min(x1a, x1b)
    if x0 >= x1:
      raise ValueError("domains do not overlap")
    
    new_segments = []
    
    for (x0a, y0a, x1a, y1a), (x0b, y0b, x1b, y1b) in zip(self.segments, rhs.segments):
        if x0b >= x0a and x1b <= x1a:
            new_segments.append((
                x0b,
                y0a + factor * y0b,
                x1b,
                y1a + factor * y1b
            ))
    
    new_pwlf = PieceWiseLinear(new_segments[0][0], new_segments[0][1], new_segments[-1][2], new_segments[-1][3])
    new_pwlf.segments = new_segments
    return new_pwlf
    
    raise NotImplementedError

  def add_number(self, rhs, factor):
    """Returns the sum of this function and factor * rhs,
where rhs is a number.
This function remains unchanged."""
    new_segments = [
        (x0, y0 + factor * rhs, x1, y1 + factor * rhs)
        for (x0, y0, x1, y1) in self.segments
    ]
    
    # Create a new PieceWiseLinear object
    new_pwlf = PieceWiseLinear(self.x0, self.y0 + factor * rhs, self.x1, self.y1 + factor * rhs)
    new_pwlf.segments = new_segments
    return new_pwlf

    raise NotImplementedError

  def __add__(self, rhs):
    """Addition of a piecewise linear function with a number or 
with another piecewise linear function.
Returns a new function, this function remains unchanged."""
    if isinstance(rhs, PieceWiseLinear):
      return self.add_pwlf(rhs, +1)
    else:
      return self.add_number(rhs, +1)

  def __sub__(self, rhs):
    """Subtraction of a number or of another piecewise linear function
from this piecewise linear function.
Returns a new function, this function remains unchanged."""
    if isinstance(rhs, PieceWiseLinear):
      return self.add_pwlf(rhs, -1)
    else:
      return self.add_number(rhs, -1)
  
# --------------------------------------------------------------------

if __name__ == "__main__":
  f1 = PieceWiseLinear(1, -1, 3, 1)
  f2 = PieceWiseLinear(3, 1, 7, -5)
  print("f1 = %s" % f1)
  print("f2 = %s" % f2)  
  for x in [1, 2, 3]:
    print("f1(%g) = %g" % (x, f1(x)))
  for x in [3, 5, 7]:
    print("f2(%g) = %g" % (x, f2(x)))
  f = f1.join(f2)
  print("f = %s" % f)  
  for x in [1, 2, 3, 5, 7]:
    print("f(%g) = %g" % (x, f(x)))
  print("Domain of f1 = %s, domain of f2 = %s, domain of f = %s" %
        (f1.domain(), f2.domain(), f.domain()))
  g1 = f + 2
  print("g1 = f + 2 = %s" % g1)
  g2 = f - 6
  print("g2 = f - 6 = %s" % g2)
  g3 = 3 * f
  print("g3 = 3 * f = %s" % g3)
  h1 = 5 * f + 3
  h2 = 0.5 * f - 2
  print("h1 = 5 * f + 3 = %s" % h1)
  print("h2 = 0.5 * f - 2 = %s" % h2)
  g = h1 + h2
  print("g = h1 + h2 = %s" % g)
  d1 = PieceWiseLinear(0, 0, 2, 19)
  d = d1.join(PieceWiseLinear(2, 19, 6, 12))
  print("d = %s" % d)
  e1 = g + d
  e2 = g - d
  print("e1 = g + d = %s" % e1)
  print("e2 = g - d = %s" % e2)  
  for x in [1, 2, 3, 4, 5, 6]:
    print("g(%g) = %g, d(%g) = %g, e1(%g) = %g, e2(%g) = %g" %
          (x, g(x), x, d(x), x, e1(x), x, e2(x)))

# --------------------------------------------------------------------
