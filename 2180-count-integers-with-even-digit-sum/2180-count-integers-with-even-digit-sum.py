class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0 
        for i in range(2,num+1):
            if  i < 10 and i % 2 == 0 :
                count += 1
            else :
                x = list(str(i))
                summ  = 0
                for j in x:
                    summ += int(j)
                if summ % 2 == 0:
                    count += 1
        return count 