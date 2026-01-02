class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(1,numRows + 1):
            if i == 1 :
                res.append([i])
            else:
                last = res[-1]
                row = [1] + [last[j] + last [j+1] for j in range(len(last)-1)] + [1]
                res.append(row) 
        return res            
