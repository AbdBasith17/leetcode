class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
       
        for i in reversed(num):
            if i == "0":
                num = num[:-1]
            else:
                return num
        return num