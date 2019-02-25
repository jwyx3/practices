* [binary search](https://zxi.mytechroad.com/blog/algorithms/binary-search/sp5-binary-search/)

```
"""
Returns the smallest number m such that g(m) is true.
[l, r)
"""
def binary_search(l, r):
  while l < r:
    m = l + (r - l) // 2
    if f(m): return m    # if m is the answer
    if g(m):
      r = m              # new range [l, m)
    else
      l = m + 1          # new range [m+1, r)
  return l               # or not found
```
