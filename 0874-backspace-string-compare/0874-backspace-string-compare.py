class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
       
        li_s = []
        li_t = []

        for i in s:
            if i == '#':
                if li_s:
                    li_s.pop()
            else:
                li_s.append(i)

        for i in t:
            if i == '#':
                if li_t:
                    li_t.pop()
            else:
                li_t.append(i)

        return "".join(li_s) == "".join(li_t)

        