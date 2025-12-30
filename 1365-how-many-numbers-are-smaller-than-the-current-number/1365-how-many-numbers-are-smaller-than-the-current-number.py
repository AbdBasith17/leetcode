class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        li = []
        count = 0
        for i in nums:
            for j in nums:
                if i != j and i > j:
                    count += 1
            li.append(count)
            count = 0
        return li            