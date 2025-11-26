class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vov = "aeiouAEIOU"
        i = len(s)//2
        a = s[:i]
        b = s[i:]

        counta = sum(1 for c in a if c in vov)
        countb = sum(1 for c in b if c in vov)

        return counta == countb