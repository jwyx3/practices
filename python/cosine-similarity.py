class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: Cosine similarity.
    """
    def cosineSimilarity(self, A, B):
        if not A or not B or len(A) != len(B):
            return 2.0
        n = len(A)
        up = sum([A[i]*B[i] for i in range(n)])
        down = sum([a*a for a in A]) * sum([b*b for b in B])
        if down == 0:
            return 2.0
        return up / math.sqrt(down)
