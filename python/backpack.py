class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size

    # dp[i][v]: the max size we can fill with i items and the backpack with v size
    # dp[i][v] = max(dp[i-1][v-A[i-1]] + A[i-1], dp[i-1][v]]
    # initial: dp[i][0] = 0, dp[0][v] = 0
    # ans: dp[n][m]
    # TLE!
    def backPack0(self, m, A):
        if m == 0 or not A or len(A) == 0:
            return 0
        n = len(A)
        dp = [[0 for v in xrange(m+1)] for i in xrange(2)]
        for i in xrange(1, n+1):
            for v in xrange(1, m+1):
                dp[i % 2][v] = dp[(i-1) % 2][v]
                if v >= A[i-1]:
                    dp[i % 2][v] = max(dp[(i-1) % 2][v-A[i-1]] + A[i-1], dp[i % 2][v])
        return dp[n % 2][m]

    # optimize: reuse same array
    # TLE!
    def backPack1(self, m, A):
        if m == 0 or not A or len(A) == 0:
            return 0
        n = len(A)
        dp = [0 for v in xrange(m+1)]
        for item in A:
            for v in xrange(m, -1, -1):
                if v >= item:
                    dp[v] = max(dp[v-item] + item, dp[v])
        return dp[m]

    # dp[v]: whether v is the valid size we can fill, 1 is valid
    # dp[v] = 1 # if dp[v-item] == 1 and v >= item
    #         0 # otherwise
    # initial: dp[0] = 1 # fill nothing
    # ans: max(dp[i]) # dp[i] == 1
    def backPack(self, m, A):
        if m == 0 or not A or len(A) == 0:
            return 0
        ans, n = 0, len(A)
        dp = [0 for v in xrange(m+1)]
        dp[0] = 1
        for item in A:
            for v in xrange(m, -1, -1):
                if v >= item and dp[v-item] == 1:
                    ans = max(ans, v)
                    dp[v] = 1
        return ans

if __name__ == '__main__':
    s = Solution()
    print s.backPack(10, [3,4,8,5]), "#", "9"
    print s.backPack(80000, [81,112,609,341,164,601,97,709,944,828,627,730,460,523,643,901,602,508,401,442,738,443,555,471,97,644,184,964,418,492,920,897,99,711,916,178,189,202,72,692,86,716,588,297,512,605,209,100,107,938,246,251,921,767,825,133,465,224,807,455,179,436,201,842,325,694,132,891,973,107,284,203,272,538,137,248,329,234,175,108,745,708,453,101,823,937,639,485,524,660,873,367,153,191,756,162,50,267,166,996,552,675,383,615,985,339,868,393,178,932]), '#', '52741'
