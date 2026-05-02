class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(' ')
        li = []
        for i in s:
            res = i[:-1] , int(i[-1])
            li.append(res)

        sortlist = sorted(li , key = lambda x:x[1] )

        t = []
        for i in sortlist:
            t.append(i[0])

        return ' '.join(t)