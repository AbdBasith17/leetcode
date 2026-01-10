class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        count = 0
        for i in range(low,high+1):
            if len(str(i)) % 2 == 0:
                s = str(i)
                l = int(len(s)/2)
                s1 = s[:l]
                s2 = s[l:]
                if sum(int(x) for x in s1) == sum(int(x) for x in s2):
                    count += 1
        return count           
                
