class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        count = 0

        s = text.split(" ")
        for i in s:
            if all (j not in i for j in list(brokenLetters)):
                count += 1
        return count
        