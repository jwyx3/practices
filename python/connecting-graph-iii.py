class ConnectingGraph3:

    # @param {int} n
    def __init__(self, n):
        # initialize your data structure here.
        self.father = [0 for i in xrange(n + 1)]
        self.count = n

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
            self.count -= 1

    # @param {int} a
    # return {int} the number of connected component
    # in the graph
    def query(self):
        return self.count
