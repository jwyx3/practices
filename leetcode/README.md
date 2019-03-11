* [input size vs algo](http://zxi.mytechroad.com/blog/sp/input-size-v-s-time-complexity/)

```
< 10: O(n!) permutation
< 15: O(2^n) combination
< 50: O(n^4) DP
< 200: O(n^3) DP, all pairs shortest path
< 1,000: O(n^2) DP, all pairs, dense graph
< 1,000,000: O(nlogn), sorting-based (greedy), heap, divide & conquer
< 1,000,000: O(n), DP, graph traversal / topological sorting (V+E), tree traversal
< INT_MAX: O(sqrt(n)), prime, square sum
< INT_MAX: O(logn), binary search
< INT_MAX: O(1) Math
```

* [time complexity of recursion](http://zxi.mytechroad.com/blog/sp/time-space-complexity-of-recursion-functions-sp4/)

```
Equation	Time	Space	Examples
T(n) = 2*T(n/2) + O(n)	O(nlogn)	O(logn)	quick_sort
T(n) = 2*T(n/2) + O(n)	O(nlogn)	O(n + logn)	merge_sort
T(n) = T(n/2) + O(1)	O(logn)	O(logn)	Binary search
T(n) = 2*T(n/2) + O(1)	O(n)	O(logn)	Binary tree traversal
T(n) = T(n-1) + O(1)	O(n)	O(n)	Binary tree traversal
T(n) = T(n-1) + O(n)	O(n^2)	O(n)	quick_sort(worst case)
T(n) = n * T(n-1)	O(n!)	O(n)	permutation
T(n) = T(n-1)+T(n-2)+…+T(1)	O(2^n)	O(n)	combination


For recursion with memorization:

Time complexity: |# of subproblems| * |exclusive running time of a subproblem|
Space complexity:|# of subproblems|  + |max recursion depth| * |space complexity of a subproblem|

Think recursion part as O(1) when we calculate exclusive running time of a subproblem
```

* [Amortized Analysis](https://zxi.mytechroad.com/blog/sp/amortized-analysis/) 

![time complexity vs amortized complexity](https://zxi.mytechroad.com/blog/wp-content/uploads/2018/09/sp7-1.png)

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

"""
Returns the largest number m such that g(m) is true.
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
  return l - 1           # or not found
```
