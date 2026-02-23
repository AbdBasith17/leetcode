class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        d = {}

        for i in range(len(releaseTimes)):
            if i == 0:
                d[i] = releaseTimes[i]
            else:
                d[i] = releaseTimes[i] - releaseTimes[i - 1]

    
        sorted_d = sorted(d.items(),key=lambda x: (x[1], keysPressed[x[0]]),reverse=True)

   
        return keysPressed[sorted_d[0][0]]