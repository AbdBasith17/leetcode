class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        q = {}
        for _,item in enumerate(s):
            if item in q:
                q[item] += 1
            else:  
                q[item] = 1

        li=[]
        lq=[]
        for i in q :
            if i in 'aeiou':
                li.append(q[i])
            else:
                lq.append(q[i])

        return (max(li) if li else 0) + (max(lq) if lq else 0)