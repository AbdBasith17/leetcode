class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        esum = sum(nums)
        dsum = 0
        for i in nums:
            for dig in str(i):
                dsum += int(dig)
        return abs(esum-dsum)         