from collections import deque


class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer

    # BFS
    def ladderLength(self, start, end, dict):
        if not dict or not start or not end or len(start) != len(end):
            return 0
        dict.add(end)
        q = deque([(start, 1)])
        while q:
            curt, curtLen = q.popleft()
            if curt == end:
                return curtLen
            for i in range(len(curt)):
                part1, part2 = curt[:i], curt[i + 1:]
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c != curt[i]:
                        word = part1 + c + part2
                        if word in dict:
                            q.append((word, curtLen + 1))
                            dict.remove(word)
        return 0
