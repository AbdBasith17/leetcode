class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = [i for i in s if i.isalpha()]
        l.reverse()

        li = []
        count = 0
        for i in s:
            if i.isalpha():
                li.append(l[count])
                count += 1
            else:
                li.append(i)

        return ''.join(li)