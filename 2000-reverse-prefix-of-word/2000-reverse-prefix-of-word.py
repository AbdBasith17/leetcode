class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        ind = 0
        for i in range(len(word)):
            if word[i] == ch:
                ind = i+1
                break
        return word[:ind][::-1] + word[ind:]

