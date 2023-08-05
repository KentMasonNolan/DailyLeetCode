class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        left, right = 0, len(s)-1

        while left < right:
            while left < right and not self.alphanum(s[left]):
                left += 1
            while left < right and not self.alphanum(s[right]):
                right -= 1
            if s[left].islower() != s[right].islower():
                return False

            left += 1
            right -= 1
        return True
