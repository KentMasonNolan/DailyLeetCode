class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hastSet = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hastSet:
                return [hastSet[diff], i]
            hastSet[n] = i
        return