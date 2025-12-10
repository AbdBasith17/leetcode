class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        if start > destination: 
            start , destination = destination ,start

        li1 = distance [start: destination]
        li2 = distance[:start] + distance[destination:]

        s = sum(li1) , sum(li2)
        return min(s)