#!/usr/bin/env python3
import bisect

class BucketSet:
  def __init__(s, keys):
    s.keys = list(sorted(keys))
    s.n = len(s.keys) + 1
    s.v = [0 for i in range(s.n)]

  def _get(s,x):
    y = 0
    while x >= 0:
      y += s.v[x]
      x = (x & (x+1)) - 1
    return y

  def add(s,x,y):
    x = bisect.bisect_left(s.keys,x)
    while x < s.n:
      s.v[x] += y
      x |= x+1

  def find_next(s,x):
    y = s._get(bisect.bisect_left(s.keys,x)-1)
    b = 2**20
    x = 0
    while b > 0:
      if (x|b)-1<len(s.v) and s.v[(x|b)-1]<=y:
        y -= s.v[(x|b)-1]
        x |= b
      b = b // 2
    return s.keys[x] if x<len(s.keys) else None

def main():
  s = BucketSet([4,5,6,7,8,9,10])
  s.add(5,1)
  s.add(6,2)
  s.add(7,1)
  print(s.find_next(5)); s.add(5,-1)
  print(s.find_next(5)); s.add(6,-1)
  print(s.find_next(5)); s.add(6,-1)
  print(s.find_next(5)); s.add(7,-1)
  print(s.find_next(5));

main()