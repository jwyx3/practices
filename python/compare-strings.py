class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """

    # hash table
    def compareStrings(self, A, B):
        if len(B) == 0:
            return True
        if len(A) == 0:
            return False
        d = [0 for _ in range(26)]
        for c in A:
            d[ord(c) - ord('A')] += 1
        for c in B:
            k = ord(c) - ord('A')
            if d[k] == 0:
                return False
            d[k] -= 1
        return True
