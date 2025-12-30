class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        li = []
        for i in range(1,n//2+1):
            li.append(i) 
            li.append(-i)
        if n%2 == 1:
            li.append(0)
        return li       
            