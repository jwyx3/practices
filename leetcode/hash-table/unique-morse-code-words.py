# https://leetcode.com/problems/unique-morse-code-words/
# https://leetcode.com/problems/unique-morse-code-words/solution/
# Time: O(N)
# Space: O(N)

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morses = [".-","-...","-.-.","-..",".","..-.","--.","....",
                  "..",".---","-.-",".-..","--","-.","---",".--.",
                  "--.-",".-.","...","-","..-","...-",".--","-..-",
                  "-.--","--.."]
        return len({''.join([morses[ord(c) - ord('a')] for c in word]) for word in words})
