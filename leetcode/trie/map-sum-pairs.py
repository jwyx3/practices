class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.total = 0 # sum of words has this prefix
        self.val = 0

class MapSum(object):
    def __init__(self):
        self.root = TrieNode()

    def search(self, key):
        """
        get value of key, return 0 if doesn't exist
        """
        node = self.root
        for c in key:
            node = node.children.get(c)
            if not node:
                return 0
        return node.val

    def insert(self, key, val):
        diff = val - self.search(key)
        node = self.root
        for c in key:
            node.total += diff
            node = node.children[c]
        node.total += diff
        node.val = val

    # = startsWith()
    def sum(self, key):
        node = self.root
        for c in key:
            node = node.children.get(c)
            if not node:
                return 0
        return node.total
