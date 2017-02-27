class Solution:
    """
    @param source: A string
    @param target: A string
    @return: A string denote the minimum window
             Return "" if there is no such a string
    """

    # O(n)
    def minWindow(self, source, target):
        if not source or not target:
            return ""
        S, T = source, target
        # dt is temporary dict, d is used to save character count in T
        d, dt = dict.fromkeys(T, 0), dict.fromkeys(T, 0)
        for c in T:
            d[c] += 1
        ans, i, j, count = "", 0, 0, 0
        for i in range(len(S)):
            # meet requirement: contain all elements in T
            while j < len(S) and count < len(T):
                # only care about the character in T
                if S[j] in dt:
                    if dt[S[j]] < d[S[j]]:
                        count += 1
                    dt[S[j]] += 1
                j += 1
            if count == len(T) and S[i] in dt and dt[S[i]] == d[S[i]]:
                if ans == "" or j - i < len(ans):
                    ans = S[i:j]
            if S[i] in dt:
                dt[S[i]] -= 1
                if dt[S[i]] < d[S[i]]:
                    count -= 1
        return ans
