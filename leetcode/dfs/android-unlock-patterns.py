# https://leetcode.com/problems/android-unlock-patterns
# https://leetcode.com/problems/android-unlock-patterns/solution/
# https://leetcode.com/problems/android-unlock-patterns/discuss/82463/Java-DFS-solution-with-clear-explanations-and-optimization-beats-97.61-(12ms)
# Time: O(N!), number of potential patten
# Spcae: O(N), call stack
# understand of knight move can be different!!

class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """    
        def isValid(i, j, visited):
            xi, yi, xj, yj = i / 3, i % 3, j / 3, j % 3
            # adjacent
            if abs(xi - xj) <= 1 and abs(yi - yj) <= 1:
                return True
            # acrocss node
            elif (i + j) % 2 == 0:
                return visited[(i + j) / 2]
            return True
            # knight move seems to be ok!
            #elif abs(xi - xj) == 2:
            #    nx = (xi + xj) / 2
            #    return visited[nx * 3 + yi] and visited[nx * 3 + yj]
            #else:
            #    ny = (yi + yj) / 2
            #    return visited[xi * 3 + ny] and visited[xj * 3 + ny]
        
        def dfs(i, rem, visited):
            if rem == 0:
                return 1
            res = 0
            visited[i] = True
            for j in xrange(9):
                if not visited[j] and isValid(i, j, visited):
                    res += dfs(j, rem - 1, visited)
            visited[i] = False
            return res
        
        res = 0
        for rem in xrange(m, n + 1):
            # symetric
            res += dfs(0, rem - 1, [False] * 10) * 4
            res += dfs(1, rem - 1, [False] * 10) * 4
            res += dfs(4, rem - 1, [False] * 10)
        return res
            
