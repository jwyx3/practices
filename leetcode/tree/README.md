### resources
1 (binary tree summary)[https://www.youtube.com/watch?v=PbGl8_-bZxI]

```
# from resource#1
Template 1: one root

func solve(root):
  if not root: return ...
  if f(root): return ...
  l = solve(root.left)
  r = solve(root.right)
  return g(root, l, r)

# LC 104. Maximum Depth of Binary Tree
# LC 111. Minimum Depth of Binary Tree
# LC 112. Path Sum

Template 2: two nodes
func solve(p, q):
  if not p and not q: return ...
  if f(p, q): return ...
  c1 = solve(p.child, q.child)
  c2 = solve(p.child, q.child)
  return g(p, q, c1, c2)

# LC 100. Same Tree
# LC 101. Symmetric Tree
# LC 951. Flip Equivalent Binary Trees
```
