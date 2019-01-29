# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/
# use array and set

class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pos = collections.defaultdict(set)
        self.nums = []

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        res = not self.pos[val]
        self.pos[val].add(len(self.nums))
        self.nums.append(val)
        return res

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if self.pos[val]:
            last = self.nums.pop()
            if last != val:
                pos = next(iter(self.pos[val]))
                self.nums[pos] = last
                self.pos[last].add(pos)
                self.pos[val].discard(pos)
            self.pos[last].discard(len(self.nums))
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        pos = random.randint(0, len(self.nums) - 1)
        return self.nums[pos]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
