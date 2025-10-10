class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        g = []
        for i in sentences:
            l = i.split()
            g.append(len(l))
        g.sort()
        return (g[-1])