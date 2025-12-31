class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        a =set()
        for i in s :
            if i in a:
                return i
            a.add(i)    