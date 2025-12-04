class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        p = "".join([ch if ch.isalpha() else " " for ch in paragraph])
        s = p.split()
        s = [w.lower() for w in s]
        s = [w for w in s if w not in banned]    

        count = [s.count(x) for x in s ]
        return s[count.index(max(count))]