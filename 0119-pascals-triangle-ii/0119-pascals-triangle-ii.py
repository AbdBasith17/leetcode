class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = []
        for i in range(rowIndex + 1):
            if i == 0 :
                res.append([1])
            else:
                last = res[-1]
                row = [1] + [last[j] + last [j+1] for j in range(len(last)-1)] + [1]
                res.append(row) 
        return res[-1]            
