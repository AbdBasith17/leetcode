class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        li = [ x for x in str(num)]
        count = 0
        for i in li:
            if num % int(i) == 0:
                count += 1
        return(count) 