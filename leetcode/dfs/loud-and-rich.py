# https://leetcode.com/problems/loud-and-rich/
# https://leetcode.com/problems/loud-and-rich/solution/
# Learn: use dfs to find min of subgraph and using memoization
# Time: O(N)
# Space: O(N)

class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        # construct direct graph graph[x] = y, y is richer
        # logically consistent -> DAG -> can use memorization
        
        graph = collections.defaultdict(list)
        for x, y in richer:
            graph[y].append(x)
        
        N = len(quiet)
        answer = [None] * N
        
        def dfs(person):
            if answer[person] is None:
                answer[person] = person
                for nei in graph[person]:
                    cand = dfs(nei)
                    if quiet[cand] < quiet[answer[person]]:
                        answer[person] = cand
            return answer[person]
        
        for p in xrange(N):
            dfs(p)
        return answer
        
