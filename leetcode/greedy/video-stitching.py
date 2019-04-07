# https://leetcode.com/problems/video-stitching/
# Time: O(NlogN)
# Space: O(1)

class Solution(object):
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        # greedy: get max end within one interval
        clips.sort()
        n = len(clips)
        ans = i = limit = 0
        while i < n:
            prev = limit
            while i < n and clips[i][0] <= prev:
                limit = max(limit, clips[i][1])
                i += 1
            ans += 1
            if limit >= T:  # stop early, T == 0
                return ans
            if prev == limit:  # can't procceed
                break
        return -1
