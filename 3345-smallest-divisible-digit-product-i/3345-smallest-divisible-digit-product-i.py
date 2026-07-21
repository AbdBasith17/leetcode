class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        while True:

            if n < 10 :
                p = n
            else:
                v = n % 10
                x = n//10
                p = x*v

            if (p) % t == 0:
                return n
                
            n +=1 

