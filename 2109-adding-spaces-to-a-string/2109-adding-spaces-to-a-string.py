class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
    
        res = []
        laix = 0
        for i in spaces:
            res.append(s[laix:i])
            res.append(" ")
            laix = i
        res.append(s[laix:])

        return("".join(res))