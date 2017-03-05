from collections import defaultdict, deque


class Solution:
    # @param {int[]} org a permutation of the integers from 1 to n
    # @param {int[][]} seqs a list of sequences
    # @return {boolean} true if it can be reconstructed only one or false

    # BFS: topological sorting
    # whether seqs can construct only superseq org
    # check whether org is only topological sorting of seqs
    def sequenceReconstruction(self, org, seqs):
        if org is None or seqs is None:
            return False
        indegree = defaultdict(int)
        # [5,2,6,3]: 2 depends on 5
        edges = defaultdict(set)
        nodes = set()
        for seq in seqs:
            nodes |= set(seq)
            for i in range(len(seq) - 1):
                if seq[i + 1] not in edges[seq[i]]:
                    indegree[seq[i + 1]] += 1
                    edges[seq[i]].add(seq[i + 1])

        # whether seqs have all nodes in org
        if len(nodes) != len(org):
            return False

        result, q = list(), deque()
        # use all integers in org
        for node in org:
            if indegree[node] == 0:
                q.append(node)
                result.append(node)

        while q:
            # only one topological sorting
            if len(q) > 1:
                return False
            curt = q.popleft()
            for node in edges[curt]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    q.append(node)
                    result.append(node)

        # the topological sorting is org
        if len(result) != len(org):
            return False
        for i in range(len(result)):
            if result[i] != org[i]:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    #print s.sequenceReconstruction([1,2,3], [[1,2],[1,3],[2,3]])
    #print s.sequenceReconstruction([4,1,5,2,6,3], [[5,2,6,3],[4,1,5,2]])
    print s.sequenceReconstruction([1], [[],[]])
