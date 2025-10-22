class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.upper()
        count = 0
        for i in range(len(list(s))-1):
            if s[i] != s[i+1]:
                count += 1
            else:
                count += 0
        return count