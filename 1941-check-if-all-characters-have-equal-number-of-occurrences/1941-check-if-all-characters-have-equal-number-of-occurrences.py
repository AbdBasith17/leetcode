class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        li = []
        for  i in s:
            li.append(s.count(i))
        return len(set(li)) == 1