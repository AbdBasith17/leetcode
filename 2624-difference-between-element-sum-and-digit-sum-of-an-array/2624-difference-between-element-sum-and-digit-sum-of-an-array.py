class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        esum = 0
        dsum = 0
        for i in nums:
            esum += i
            for dig in str(i):
                 dsum += int(dig)
        return abs(esum-dsum)         