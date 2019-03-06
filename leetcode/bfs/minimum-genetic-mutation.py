# https://leetcode.com/problems/minimum-genetic-mutation/
# Time: O(V + E)
# Space: O(V), q size

class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        # BFS
        if not start or not end:
            return -1
        if start == end:
            return 0
        
        letters = ('A', 'C', 'G', 'T')
        bank = set(bank)
        
        def neighbors(word):
            for i, c in enumerate(word):
                for nc in letters:
                    if nc == c:
                        continue
                    new_word = word[:i] + nc + word[i+1:]
                    if new_word in bank:
                        yield new_word
            
        visited = set([start])
        q = collections.deque([start])
        ans = 0
        while q:
            ans += 1
            size = len(q)
            for _ in xrange(size):
                curr = q.popleft()
                for nei in neighbors(curr):
                    if nei in visited:
                        continue
                    if nei == end:
                        return ans
                    visited.add(nei)
                    q.append(nei)
        return -1

