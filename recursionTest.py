# recursion test

import sys

sys.setrecursionlimit(1500)

def zz(x):
  if x < 1: return 0
  result = zz(x-1) + x
  return result

print zz(1200)
