"""
Definition of Column:
class Column:
    def __init__(self, key, value):
        self.key = key
        self.value = value
"""


class MiniCassandra:
    def __init__(self):
        # initialize your data structure here.
        self.client = {}

    # @param {string} raw_key a string
    # @param {int} column_key an integer
    # @param {string} column_value a string
    # @return nothing
    def insert(self, raw_key, column_key, column_value):
        # Write your code here
        new_col = Column(column_key, column_value)
        if raw_key not in self.client:
            self.client[raw_key] = []
        index = 0
        while index < len(self.client[raw_key]):
            col = self.client[raw_key][index]
            if new_col.key == col.key:
                self.client[raw_key][index] = new_col
                break
            elif new_col.key < col.key:
                self.client[raw_key].insert(index, new_col)
                break
            index += 1
        if index == len(self.client[raw_key]):
            self.client[raw_key].append(new_col)

    # @param {string} raw_key a string
    # @param {int} column_start an integer
    # @param {int} column_end an integer
    # @return {Column[]} a list of Columns
    def query(self, raw_key, column_start, column_end):
        # Write your code here
        result = []
        if raw_key not in self.client:
            return result
        for col in self.client[raw_key]:
            if col.key >= column_start and col.key <= column_end:
                result.append(col)
        return result

