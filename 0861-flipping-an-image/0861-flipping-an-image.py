class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
  
        result = []  
        for row in image: 
            rev_row = list(reversed(row))
            inverted = []
            for i in rev_row:
                inverted.append(1 - i)
            result.append(inverted)
        
        return result

