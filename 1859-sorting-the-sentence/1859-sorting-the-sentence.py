class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        s.sort(key = lambda x : int(x[-1]))

        return ' '.join(w[:-1] for w in s )