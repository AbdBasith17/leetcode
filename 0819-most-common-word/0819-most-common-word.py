class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        p = "".join([ch if ch.isalpha() else " " for ch in paragraph])
        s = p.split()
        if banned == []:
            s = [w.lower() for w in s] 
        elif len(banned)> 1:    
            s = [w.lower() for w in s if w.lower() not in banned]
        else:
            s = [ w.lower() for w in s if w.lower() != banned[0]]    

        count = [s.count(x) for x in s ]
        return s[count.index(max(count))]