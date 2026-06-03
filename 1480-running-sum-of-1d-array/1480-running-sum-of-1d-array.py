class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        li = []
        s = 0
        for i in range(len(nums)):
            s = nums[i]+s
            li.append(s) 
        return li 