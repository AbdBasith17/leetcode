class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        
        pairs = []
        for i in range(len(names)):
            pairs.append([heights[i], names[i]])
    
        pairs.sort(reverse=True)

        return [p[1] for p in pairs]