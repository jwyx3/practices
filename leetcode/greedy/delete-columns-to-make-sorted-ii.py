# https://leetcode.com/problems/delete-columns-to-make-sorted-ii/
# Time: O(len(A)*len(A[0]))
# Space: O(len(A)*len(A[0]))

# use dict
class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        if not A:
            return 0
        M = len(A[0])
        res, g = 0, {'': A} 
        for i in xrange(M):
            ng = collections.defaultdict(list)
            valid, unique = True, True
            for k, words in g.iteritems():
                ng[k + words[0][i]].append(words[0])
                for j in xrange(1, len(words)):
                    # need to delete or not
                    if valid and words[j][i] < words[j - 1][i]:
                        valid = False
                        res += 1
                    # prepare next index
                    nk = k + words[j][i]
                    if nk in ng:
                        unique = False
                    ng[nk].append(words[j])
            # keep this index
            if valid:
                # if no possible conflict, stop
                if unique:
                    break
                g = ng
        return res

# can still be optimized to using array to remember last same indices
# because the number of same indices are reducing
# refer: https://leetcode.com/problems/delete-columns-to-make-sorted-ii/solution/
