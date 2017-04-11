class Solution:
    # @param {string} s a string
    # @param {set} dict a set of n substrings
    # @return {int} the minimum length

    # go through solution space tree and find the min
    def minLength(self, s, dict):
        import collections
        q = collections.deque([s])
        visited = set([s])
        ans = len(s)

        while q:
            s = q.popleft()
            for sub in dict:
                found = s.find(sub)
                while found != -1:
                    new_s = s[:found] + s[found + len(sub):]
                    if new_s not in visited:
                        if len(new_s) < ans:
                            ans = len(new_s)
                        q.append(new_s)
                        visited.add(new_s)
                    found = s.find(sub, found + 1)
        return ans


if __name__ == '__main__':
    s = Solution()
    print s.minLength("abcabd", ["ab","abcd"])
