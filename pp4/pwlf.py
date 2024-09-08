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
            segment_strs.append("(%g,%g)" % (x0,y0))
        # Append the ending point of the current segment
        segment_strs.append("(%g,%g)" % (x1,y1))
    result = segment_strs
    return "..".join(result)
    raise NotImplementedError

  def __call__(self, x):
    """Evaluate this function at x-coordinate x."""
    d = self.domain()
    if x < d[0] or x > d[1]:
      raise ValueError("argument is not in domain")
    # f.segment = [(1, -1, 3, 1), (3, 1, 7, -5)]
   
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
    
    d1= self.domain() #(1, 3)
    d2 = rhs.domain() #(3, 7)
    if d1[1] != d2[0]:
      raise ValueError("domains are not contiguous")
    if abs(self(d1[1]) - rhs(d2[0])) > 1e-13:
      raise ValueError("discontinuity at connection point")
    
    new_segments = self.segments + rhs.segments
    new_pwlf = PieceWiseLinear(new_segments[0][0], new_segments[0][1], new_segments[-1][2], new_segments[-1][3])
    new_pwlf.segments = new_segments
    
    return new_pwlf
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

    # Create a list of x-values (breakpoints) from both functions
    x_values = set()
    for (x0_self, _, x1_self, _) in self.segments:
        if x0 <= x1_self and x1 >= x0_self:
            x_values.update([x0_self, x1_self])
    for (x0_rhs, _, x1_rhs, _) in rhs.segments:
        if x0 <= x1_rhs and x1 >= x0_rhs:
            x_values.update([x0_rhs, x1_rhs])
    
    # Sort the x-values to determine the new breakpoints
    x_values = sorted(x for x in x_values if x0 <= x <= x1)
    
    new_segments = []
    
    # Iterate over the new breakpoints and calculate new y-values
    for i in range(len(x_values) - 1):
        x_start = x_values[i]
        x_end = x_values[i + 1]
        
        # Calculate y-values for self
        y_start_self = self.__call__(x_start)
        y_end_self = self.__call__(x_end)
        
        # Calculate y-values for rhs
        y_start_rhs = rhs.__call__(x_start)
        y_end_rhs = rhs.__call__(x_end)
        
        # Add the values (self + factor * rhs)
        y_start = y_start_self + factor * y_start_rhs
        y_end = y_end_self + factor * y_end_rhs
        
        # Add the new segment to the list
        new_segments.append((x_start, y_start, x_end, y_end))
    
    # Create a new PieceWiseLinear function with the new segments
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
