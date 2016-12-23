class TrieNode(object):
    def __init__(self, is_word=False):
        self.is_word = is_word
        self.children = {}


class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        if len(board) == 0:
            return False
        if len(board[0]) == 0:
            return False

        n, m = len(board), len(board[0])
        # build trie from word
        root_node = TrieNode()
        curr_node = root_node
        for x in word:
            curr_node.children[x] = curr_node.children.get(x, TrieNode())
            curr_node = curr_node.children[x]
        curr_node.is_word = True

        delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def search(parent_node, x, y, visited):
            ans = False
            if board[x][y] in parent_node.children:
                node = parent_node.children[board[x][y]]
                if not node.children:
                    return node.is_word

                visited.add((x, y))
                for dx, dy in delta:
                    nx, ny = x + dx, y + dy
                    if nx >= 0 and nx < n and ny >= 0 and ny < m and (nx, ny) not in visited:
                        if search(node, nx, ny, visited):
                            ans = True
                            break
                visited.remove((x, y))
            return ans

        for x in xrange(n):
            for y in xrange(m):
                if search(root_node, x, y, set()):
                    return True
        return False

if __name__ == '__main__':
    s = Solution()
    print s.exist(["ABCE","SFES","ADEE"], "ABCESEEEFS")
    #print s.exist(["z"], "z")
