class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        hastset = set()

        for n in nums:
            if n in hastset:
                return True
            hastset.add(n)
        return False
