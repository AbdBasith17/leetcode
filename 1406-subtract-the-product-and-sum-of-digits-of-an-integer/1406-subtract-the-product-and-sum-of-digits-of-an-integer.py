
class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        prod = 1
        li = [ int(x) for x in str(n)] 
        for i in li:
            prod *= i
        return prod - sum(li)
        