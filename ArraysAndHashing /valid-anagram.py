class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        countT, countS = {}, {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1

        for j in countS:
            if countS[j] != countT.get(j, 0):
                return False
        return True

# I should do this better and not the short way.
