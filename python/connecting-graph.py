class ConnectingGraph:

    # @param {int} n
    def __init__(self, n):
        # initialize your data structure here.
        self.father = [0 for i in xrange(n + 1)]

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

    # @param {int} a, b
    # return {boolean} true if they are connected or false
    def query(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        return ra != 0 and ra == rb
