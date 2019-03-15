# https://leetcode.com/problems/dota2-senate/
# https://leetcode.com/problems/dota2-senate/solution/
# Time: O(N), each vote remove one senate
# Space: O(N)

class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        q = collections.deque()
        people, ban = [0] * 2, [0] * 2
        for p in senate:
            i = int(p == 'R')
            people[i] += 1
            q.append(i)

        while all(people):
            i = q.popleft()
            if ban[i]:  # if i is banned
                ban[i] -= 1
                people[i] -= 1
            else:
                ban[i^1] += 1
                q.append(i)
        return 'Radiant' if people[1] else 'Dire'
