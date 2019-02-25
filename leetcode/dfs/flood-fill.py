# https://leetcode.com/problems/flood-fill/
# Time: O(N*M)
# Spcae: O(1)

class Solution(object):
    def floodFill(self, image, sr, sc, new_color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if not image or image[sr][sc] == new_color:
            return image
        N, M = len(image), len(image[0])
        
        def dfs(r, c, src_color):
            if r < 0 or r >= N or c < 0 or c >= M or image[r][c] != src_color:
                return
            image[r][c] = new_color
            dfs(r+1, c, src_color)
            dfs(r-1, c, src_color)
            dfs(r, c+1, src_color)
            dfs(r, c-1, src_color)
                
        dfs(sr, sc, image[sr][sc])
        return image
