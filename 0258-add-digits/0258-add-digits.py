class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        total = sum(int(no) for no in str(num))
        if total < 10:
            return total 
        else:
            return self.addDigits(total)



