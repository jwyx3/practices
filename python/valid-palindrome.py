class Solution:
    # @param {string} s A string
    # @return {boolean} Whether the string is a valid palindrome

    # O(n)
    def isPalindrome(self, s):
        if s is None:
            return False
        if len(s) == 0:
            return True
        left, right = 0, len(s) - 1
        # left: the index of first alphanumeric character
        # right: the index of last alphanumeric character
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left +=1
            right -= 1
        return True
