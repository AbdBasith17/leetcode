class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        n = max(a,b)
        li = []
        for i in range(1,n+1):
            if a % i ==0 and b %i ==0:
                li.append(i)
        return len(li)
