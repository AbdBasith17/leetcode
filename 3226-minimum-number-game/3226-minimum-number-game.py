class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()  
        rev = []
        for i in range(0, len(nums) - 1, 2):
            alice = nums[i]
            bob = nums[i+1]
            rev.append(bob)
            rev.append(alice)
        return rev
