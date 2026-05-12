class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c = s.count(s[0])    
        for i in s:
            r = s.count(i)          
            if r != c:
                return False
        return True 