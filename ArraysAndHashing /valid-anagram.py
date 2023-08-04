class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if sorted(s) == sorted(t):
            return True
        return False

# I should do this better and not the short way.
