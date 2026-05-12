class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        li = []

        for i in nums:
            c = [ int(x) for x in str(i)]
            li = li + c 
        return li