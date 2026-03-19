class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        rev = list(x)
        rev.reverse()
        rev = ''.join(rev)

        return x == rev

