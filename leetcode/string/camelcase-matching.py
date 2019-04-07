# https://leetcode.com/problems/camelcase-matching/
# Time: O(N*len(p) + sum(len(q)))
# Space: O(N), result size

class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        ans = []
        for query in queries:
            plen, qlen = len(pattern), len(query), 
            i = j = 0
            while i < plen and j < qlen:
                if pattern[i] == query[j]:
                    i += 1
                    j += 1
                elif query[j].islower():
                    j += 1
                else:  # can't skip upper case
                    break
            # go through remaining lower case
            while j < qlen and query[j].islower():
                j += 1
            ans.append(i == plen and j == qlen)
        return ans
                
