# https://leetcode.com/problems/pyramid-transition-matrix/
# https://leetcode.com/problems/pyramid-transition-matrix/solution/
# Time: O(L**N), L = len(letters)
# Space: O(N**2), call stacks * length of path

class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        graph = collections.defaultdict(set)
        for x, y, z in allowed:
            graph[x, y].add(z)

        # use dfs to generate next state
        def build(s, i, path):
            if i + 1 == len(s):
                yield ''.join(path)
            else:
                for c in graph[s[i], s[i+1]]:
                    path.append(c)
                    for ns in build(s, i + 1, path):
                        yield ns
                    path.pop()
        # check any of next states can be solved or not
        memo = {}
        def solve(s):
            if len(s) == 1:
                return True
            if s in memo:
                return memo[s]
            memo[s] = any(solve(cand) for cand in build(s, 0, []))
            return memo[s]
        
        return solve(bottom)
