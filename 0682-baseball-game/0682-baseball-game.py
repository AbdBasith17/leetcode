class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        li = []
        for i in operations:
            if i == "C":
                li.pop()
            elif i == "D":
                li.append(2*li[-1])
            elif i == "+":   
                 li.append(li[-1] +li[-2] )  
            else :
                li.append(int(i))       
        return sum(li)          
