import sys
from collections import deque


# BFS and DFS, refer to jiuzhang answers
class Solution1:
    # @param start, a string
    # @param end, a string
    # @param dic, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dic):
        if start is None or end is None or len(start) != len(end) or dic is None:
            return []
        dic.add(end)
        dic.add(start)
        self.buildIndexes(len(start), dic)
        self.buildDistances(end, start)
        self.ans = []
        self.generatePaths(start, end, [start])
        return self.ans

    def getKey(self, word, i):
        return word[:i] + word[i + 1:]

    def buildIndexes(self, length, dic):
        self.indexes = []
        for i in xrange(length):
            index = {}
            for word in dic:
                key = self.getKey(word, i)
                words = index.get(key, [])
                words.append(word)
                index[key] = words
            self.indexes.append(index)

    def nextWord(self, word):
        for i in xrange(len(word)):
            key = self.getKey(word, i)
            if key in self.indexes[i]:
                for w in self.indexes[i][key]:
                    if w != word:
                        yield w

    # BFS
    def buildDistances(self, start, end):
        self.distances = {}
        self.distances[start] = 0
        q = deque([start])
        while len(q) > 0:
            curt = q.popleft()
            for word in self.nextWord(curt):
                if word not in self.distances:
                    self.distances[word] = self.distances[curt] + 1
                    q.append(word)

    # DFS: path has curt
    def generatePaths(self, curt, target, path):
        if curt == target:
            self.ans.append(path[:])
            return

        for word in self.nextWord(curt):
            if self.distances.get(word, -2) + 1 == self.distances.get(curt, -2):
                path.append(word)
                self.generatePaths(word, target, path)
                path.pop()


# WRONG!!
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dic):
        if not start or not end or not dic:
            return []
        self._cache = {}
        self._diff_cache = {}
        dic.add(end)
        # remove start to avoid error using memorization
        dic.remove(start)
        ans, _ =  self.dfs(start, end, dic)
        return [x.split('#') for x in ans]

    # return all shortest transformation sequences from start to end
    def dfs(self, start, end, dic):
        key = "{}#{}".format(start, end)
        if key in self._cache:
            return self._cache[key]

        if start == end:
            return [end], 1
        ans, ansLen = [], sys.maxint
        for word in list(dic):
            if self.hasOneDiffLetter(start, word):
                dic.remove(word)
                paths, pathLen = self.dfs(word, end, dic)
                if pathLen != sys.maxint:
                    if pathLen == ansLen:
                        ans.extend(paths)
                    elif pathLen < ansLen:
                        ansLen = pathLen
                        ans = paths
                dic.add(word)
        # If no path is found, don't cache
        if ansLen != sys.maxint:
            self._cache[key] = (["{}#{}".format(start, x) for x in set(ans)], ansLen + 1)
            return self._cache[key]
        return ans, ansLen

    def hasOneDiffLetter(self, word1, word2):
        key = "{}#{}".format(word1, word2)
        if key in self._diff_cache:
            return self._diff_cache[key]

        count = 0
        for i in xrange(len(word1)):
            if word1[i] != word2[i]:
                count += 1
        self._diff_cache[key] = count == 1
        return self._diff_cache[key]

if __name__ == '__main__':
    s = Solution1()
    # print s.findLadders("a", "c", ["a","b","c"])
    print s.findLadders("hit", "cog", set(["hot","dot","dog","lot","log"]))
    # print s.findLadders("game", "thee", set(["frye","heat","tree","thee","game","free","hell","fame","faye"]))
    # print s.findLadders("kiss", "tusk", set(["miss","dusk","kiss","musk","tusk","diss","disk","sang","ties","muss"]))
    # print s.findLadders("qa", "sq", set(["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]))
