class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = int(len(s)/2) 
        a = s[:i]
        b = s[i:]
        counta = 0
        countb = 0
        for x in a:
            if any (c in x for c in "aeiouAEIOU"):
                counta += 1
        for x in b:
            if any (c in x for c in "aeiouAEIOU"):
                countb += 1
        return (counta == countb)