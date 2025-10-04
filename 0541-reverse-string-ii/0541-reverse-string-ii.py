class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        li = list(s)
        for strt in range(0,len(li),2*k):
            rev = li[strt : strt+k]
            rev.reverse()
            li[strt:strt+k] = rev
        return ''.join(li)      


    
