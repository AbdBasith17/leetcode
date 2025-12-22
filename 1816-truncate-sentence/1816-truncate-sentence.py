class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        li = s.split(" ")  
        return ''+join(li[:k])  