class Solution(object):
    def isBalanced(self, num):
        """
        :type num: str
        :rtype: bool
        """
        even = []
        odd = []

        for i in range(len(num)):
            if i % 2 == 0:
                even.append(int(num[i]))
            else:
                odd.append(int(num[i])) 
        

        return sum(even) == sum(odd)