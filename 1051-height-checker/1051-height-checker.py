class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        sort  = sorted(heights)
        s = 0
        if heights == sort :
            return 0
        else:
            for i in range(len(heights)):
                if heights[i] != sort[i]:
                    s += 1
                else:
                    pass    
        return s