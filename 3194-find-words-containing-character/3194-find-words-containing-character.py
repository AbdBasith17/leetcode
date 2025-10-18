class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        out = []
        for i, w in enumerate(words):
            if x in w :
                out.append(i)
        return out        