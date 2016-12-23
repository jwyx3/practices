class TrieNode(object):
    def __init__(self, is_word=False):
        self.is_word = is_word
        self.children = {}


class Solution:
    # @param board, a list of lists of 1 length string
    # @param words: A list of string
    # @return: A list of string
    def wordSearchII(self, board, words):
        # corner case
        if len(board) == 0 or len(board[0]) == 0:
            return []

        n, m = len(board), len(board[0])
        # create trie
        root_node = TrieNode()
        for word in words:
            curr_node = root_node
            for x in word:
                curr_node.children[x] = curr_node.children.get(x, TrieNode())
                curr_node = curr_node.children[x]
            curr_node.is_word = True

        delta = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        def search(parent_node, x, y, visited, found, ans):
            if board[x][y] in parent_node.children:
                node = parent_node.children[board[x][y]]
                found += board[x][y]
                if node.is_word:
                    # 处理可能的前缀
                    ans.add(found)
                if not node.children:
                    # 叶子节点结束
                    return

                visited.add((x, y))
                for dx, dy in delta:
                    nx, ny = x + dx, y + dy
                    if nx >= 0 and nx < n and ny >= 0 and ny < m and (nx, ny) not in visited:
                        search(node, nx, ny, visited, found, ans)
                visited.remove((x, y))

        ans = set()
        for x in xrange(n):
            for y in xrange(m):
                search(root_node, x, y, set(), '', ans)
        return list(ans)
