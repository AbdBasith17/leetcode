class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        string = str(num)
        total = sum(int(no) for no in string)
        if total < 10:
            return total 
        else:
            return self.addDigits(total)



