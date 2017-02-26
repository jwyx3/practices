class TwoSum(object):

    def __init__(self):
        # initialize your data structure here
        self.counter = {}


    # Add the number to an internal data structure.
    # @param number {int}
    # @return nothing
    def add(self, number):
        self.counter[number] = self.counter.get(number, 0) + 1


    # Find if there exists any pair of numbers which sum is equal to the value.
    # @param value {int}
    # @return true if can be found or false
    def find(self, value):
        for num, count in self.counter.items():
            rest = value - num
            if rest in self.counter:
                if rest == num and self.counter[rest] < 2:
                    continue
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)
