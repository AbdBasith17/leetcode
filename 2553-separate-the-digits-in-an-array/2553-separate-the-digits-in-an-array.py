class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        li = []

        for i in nums:
            li += [int(x) for  x in str(i)]

        return li