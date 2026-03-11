class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = bin(n)[2:]
        res = ""
        for i in n:
            if i == "1":
                res += "0"
            elif i == "0":
                res += "1"
        return int(res,2)              