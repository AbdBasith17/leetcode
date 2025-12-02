class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        dif = high - low
        if high % 2 == 0 and low % 2 == 0:
            return dif/ 2
        else:
            return  dif / 2 + 1    
        
        