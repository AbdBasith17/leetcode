class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = set()
        for i in s:
            if i.isdigit():
                l.add(i)
        l= sorted(l,reverse =True)
        if len(l)<2:
            return -1
        else:
            return int(l[1])    