#
# Print an integer in any base
#

def print_base_8(n):
  if n >= 8:
    print_base_8(n // 8)
  print(n % 8, end="")

DIGITS = "0123456789abcdef"
MAX_BASE = len(DIGITS)

# Precondition: n >= 0, 2 <= base <= 16
def print_rec(n, base):
  if n >= base:
    print_rec(n // base, base)
  digit = n % base
  print(DIGITS[digit], end="")

# Driver function
def print_in_base(n, base):
  if not (2 <= base <= MAX_BASE):
    print("Cannot print in base", base)
  else:
    if n < 0:
      print("-", end="")
      n = -n
    print_rec(n, base)
    print()

for base in range(0, 18):
  print_in_base(1000, base)

print_in_base(10000000000000000000000, 2)
print_in_base(10000000000000000000000, 16)
print_in_base(10000000000000000000000, 10)



