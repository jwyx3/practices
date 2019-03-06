# https://leetcode.com/problems/sequence-reconstruction/
# topological sorting -> MLE!!
# https://leetcode.com/problems/sequence-reconstruction/discuss/92574/Very-short-solution-with-explanation
# Time: O(N + M), N = len(org), M = len(seqs)
# Space: O(N + sum(len(seq) for seq in seqs))

# Topological sorting
class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        degree = collections.Counter()
        graph = collections.defaultdict(set)
        visited = set()
        for edge in seqs:
            # handle empty list
            if not edge:
                continue
            # the number of list may be more than 2
            n = len(edge)
            visited.add(edge[-1])
            for i in xrange(n - 1):
                visited.add(edge[i])
                for j in xrange(i + 1, n):
                    if edge[j] not in graph[edge[i]]:
                        degree[edge[j]] += 1
                        graph[edge[i]].add(edge[j])
        # need to contain all numbers of org
        if len(visited) != len(org):
            return False
        q = collections.deque()
        # iterate all numbers
        for u in org:
            if degree[u] == 0:
                q.append(u)
        if len(q) != 1:
            return False
        i = 0
        while q:
            size = len(q)
            if size > 1:
                break
            u = q.popleft()
            if u != org[i]:
                break
            i += 1
            for nei in graph[u]:
                degree[nei] -= 1
                if degree[nei] == 0:
                    q.append(nei)
        return i == len(org)

# all seq should be subsequence of org; all consecutive elements in org should be consecutive elements in seqs
# lots of corner cases:
# [1], [[1,1]]
# [1], [[], []]

class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        pairs = {}
        idx = {}
        # all elements are unique
        for i, x in enumerate(org):
            idx[x] = i
        
        # check seq are subsequence of org and create pairs
        for seq in seqs:
            for i in xrange(len(seq)):
                if seq[i] not in idx:
                    return False
                # make sure that seqs contains all elements in org
                # (seq[i], seq[i)] is invalid, so use (0, seq[i])
                pairs[0, seq[i]] = 1
                if i > 0:
                    # if seq[i - 1] == seq[i], it's invalid
                    if idx[seq[i - 1]] >= idx[seq[i]]:
                        return False
                    pairs[seq[i - 1], seq[i]] = 1
        
        # check whether any consecutive elements are pairs in seqs
        for i in xrange(len(org)):
            if (org[i - 1] if i > 0 else 0, org[i]) not in pairs:
                return False
        return True
