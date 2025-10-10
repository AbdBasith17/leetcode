class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        g = []
        for i in sentences:
            g.append(len(i.split()))
        g.sort()
        return (g[-1])