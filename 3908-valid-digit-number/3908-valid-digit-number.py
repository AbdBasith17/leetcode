class Solution(object):
    def validDigit(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: bool
        """
        
        n1 = str(n)
        x1 = str(x)
        return int(n1[0]) != x and x1 in n1 