class Solution(object):
    def isBalanced(self, num):
        """
        :type num: str
        :rtype: bool
        """
        even = 0
        odd = 0

        for i , v in enumerate(num):
            if i %2 ==0:
                even += int(v)
            else:
                odd += int(v)
        return even == odd