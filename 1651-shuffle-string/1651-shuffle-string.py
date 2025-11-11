class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        a = sorted(zip(indices,s))
        w = ''.join([i for _, i in a])
        return w