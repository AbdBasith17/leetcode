class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ssum = 0
        dsum = 0
        tsum = sum(nums)
        for i in nums:
            if i < 10:
                ssum += i
            else:
                dsum += i
        achoice1  = ssum
        bchoice1 = tsum-ssum

        achoice2  = dsum
        bchoice2 = tsum - dsum

        return achoice1 > bchoice1 or achoice2 > bchoice2


                        
