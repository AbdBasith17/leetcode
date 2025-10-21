class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ssum = sum(x for x  in nums if x < 10)
        dsum = sum(x for x  in nums if x >10)
        tsum = sum(nums)
        achoice1  = ssum
        bchoice1 = tsum-ssum

        achoice2  = dsum
        bchoice2 = tsum - dsum

        return achoice1 > bchoice1 or achoice2 > bchoice2


                        
