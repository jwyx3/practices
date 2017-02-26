'''
Definition of Document
class Document:
    def __init__(self, id, cotent):
        self.id = id
        self.content = content
'''
class Solution:
    # @param {Document[]} docs a list of documents
    # @return {dict(string, int[])} an inverted index
    def invertedIndex(self, docs):
        # Write your code here
        ans = {}
        for doc in docs:
            visited = {}
            for word in doc.content.split():
                if word not in ans:
                    ans[word] = []
                if word not in visited:
                    visited[word] = True
                    ans[word].append(doc.id)
        return ans

