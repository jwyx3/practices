import random


class Solution:

    # @param {int} n a positive integer
    # @param {int} k a positive integer
    # @return {Solution} a Solution object
    @classmethod
    def create(cls, n, k):
        # Write your code here
        solution = cls()
        solution.machines = {}
        solution.shards = []
        solution.n = n
        solution.k = k
        return solution

    # @param {int} machine_id an integer
    # @return {int[]} a list of shard ids
    def addMachine(self, machine_id):
        # write your code here
        result = []
        for i in xrange(0, self.k):
            shard = None
            while shard is None or shard in self.machines:
                shard = random.randint(0, self.n - 1)
            self.machines[shard] = machine_id
            self.shards.append(shard)
            result.append(shard)
        self.shards.sort()
        return result

    # @param {int} hashcode an integer
    # @return {int} a machine id
    def getMachineIdByHashCode(self, hashcode):
        # write your code here
        if len(self.shards) == 0:
            return -1

        result = self.machines[self.shards[0]]
        for shard in self.shards:
            if shard >= hashcode:
                result = self.machines[shard]
                break
        return result
