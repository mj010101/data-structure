#
# Calculator
#

import tokens
import math

class InputError(Exception):
  def __init__(self, msg, token):
    self.msg = msg
    self.token = token

def parse_item(tok):
  t = tok[0]
  tok.pop(0)
  if t.isNumber():
    return t.value
  if t.isIdentifier():
    if t.value == "pi":
        return math.pi
    elif t.value == "e":
        return math.e
    else:
        raise InputError("Unknown identifier", t)
  if t.isSymbol("|"):  # 절대값 연산자 처리
    expr = parse_expression(tok)
    if not tok[0].isSymbol("|"):
        raise InputError("Expected '|' to close absolute value", tok[0])
    tok.pop(0)
    return abs(expr)
  if not t.isSymbol("("):
    raise InputError("Expected number, variable, or '('", t)
  expr = parse_expression(tok)
  if not tok[0].isSymbol(")"):
    raise InputError("Expected operator or ')'", tok[0])
  tok.pop(0)
  return expr

def parse_factor(tok):
  t = tok[0]
  sign = -1 if t.isSymbol("-") else +1
  if t.isSymbol("+") or sign < 0:
    tok.pop(0)
  result = parse_item(tok)
  while tok[0].isSymbol("^"):
    tok.pop(0)
    rhs = parse_factor(tok)
    result = result ** rhs
  return sign * result
  
def parse_term(tok):
  result = parse_factor(tok)
  t = tok[0]
  while t.isSymbol("*") or t.isSymbol("/"):
    tok.pop(0)
    rhs = parse_factor(tok)
    if t.isSymbol("/"):
      if rhs == 0:
        raise InputError("Division by zero", t)
      result = result / rhs
    else:
      result = result * rhs
    t = tok[0]
  return result

def parse_expression(tok):
  result = parse_term(tok)
  t = tok[0]
  while t.isSymbol("+") or t.isSymbol("-"):
    tok.pop(0)
    rhs = parse_term(tok)
    if t.isSymbol("+"):
      result = result + rhs
    else:
      result = result - rhs
    t = tok[0]
  return result

def parse(s):
  toks = tokens.tokenize(s)
  result = parse_expression(toks)
  if not toks[0].isStop():
    raise InputError("Expected operator or end of input", toks[0])
  return result

# --------------------------------------------------------------------

if __name__ == "__main__":
  print("Welcome to KAIST Supercalculator v0.2")
  while True:
    s = input("Enter an expression: ")
    if s is None or s.strip() == "":
      break
    try:
      value = parse(s)
      print("==> %g" % value)
    except InputError as e:
      print("Error:", e.msg)
      print(s)
      print(" " * e.token.pos + "^")

# --------------------------------------------------------------------
