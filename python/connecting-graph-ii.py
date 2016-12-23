class ConnectingGraph2:

    # @param {int} n
    def __init__(self, n):
        self.father = [0 for i in xrange(n + 1)]
        self.counter = [1 for i in xrange(n + 1)]

    def find(self, a):
        if self.father[a] == 0:
            return a
        self.father[a] = self.find(self.father[a])
        return self.father[a]

    # @param {int} a, b
    # return nothing
    def connect(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra != rb:
            self.father[ra] = rb
            self.counter[rb] += self.counter[ra]

    # @param {int} a
    # return {int}  the number of nodes connected component
    # which include a node.
    def query(self, a):
        ra = self.find(a)
        return self.counter[ra]

