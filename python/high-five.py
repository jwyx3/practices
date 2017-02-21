'''
Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
'''
from heapq import heappush, heappop


# use heap
class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        # Write your code here
        students = {}
        for record in results:
            if record.id not in students:
                students[record.id] = []
            scores = students[record.id]
            heappush(scores, record.score)
            if len(scores) > 5:
                heappop(scores)
        ans = {}
        for student, scores in students.items():
            ans[student] = 1.0 * sum(scores) / len(scores)
        return ans
