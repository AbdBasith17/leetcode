class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        s = {}
        for i,num in enumerate(nums):
            if num in s and i - s[num] <= k:
                return True
            s[num] = i    
        return False    
                    



        