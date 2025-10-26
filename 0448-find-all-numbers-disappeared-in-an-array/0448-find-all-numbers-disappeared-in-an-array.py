class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sett = set(range(1,len(nums)+1))
        res = sett- set(nums)
        return list(res)  
