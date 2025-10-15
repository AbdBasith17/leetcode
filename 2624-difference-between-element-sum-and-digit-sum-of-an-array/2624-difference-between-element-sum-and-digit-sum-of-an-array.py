class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        esum = sum(nums)
        dsum = sum(int(dig) for i in nums for dig in str(i))
        return abs(esum-dsum)         