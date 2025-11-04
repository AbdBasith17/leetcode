class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        for i in range(len(s)):
            x = s[i:] + s[:i]
            if x == goal:
                return True
        return False