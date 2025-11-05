class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        address = list(address)
        for i,v in enumerate(address):
            if v == '.':
                address[i] = '[.]'
        return ''.join(address)        