# https://leetcode.com/problems/russian-doll-envelopes/
# https://www.youtube.com/watch?v=S9oUiVYEq7E
# review of LIS:
# dp[i]: the index of smallest element for LIS with length i + 1.
# prev[i]: the index of previous element for LIS ending with A[i]
# if answer is length of LIS: len(dp)
# if anwwer is LIS, then using prev to construct answer
#
# Time: O(nlogn)
# Space: O(n)
#
# sort (width, -height) to convert into LIS problem
# dp is not LIS.

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key=lambda (w, h): (w, -h))
        heights = [e[1] for e in envelopes]
        # dp[i]: smallest last element of LIS with length i + 1.
        dp = []
        N = len(heights)
        prev = [-1] * N
        
        def get_seq():
            seq = []
            if dp:
                pos = dp[-1][1]
                while pos >= 0:
                    seq.append(envelopes[pos])
                    pos = prev[pos]
                seq = seq[::-1]
            return seq

        for i, h in enumerate(heights):
            pos = bisect.bisect_left(dp, (h, -1))
            if pos >= len(dp):
                dp.append((h, i))
            elif dp[pos][0] > h:
                dp[pos] = (h, i)
            # uncomment to get LIS.
            #if pos > 0:
            #    prev[i] = dp[pos-1][1]
        # print get_seq()
        return len(dp) 
