class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        li = []
        for i in range(len(operations)):
            if operations[i] == "C":
                li.remove(li[-1])
            elif operations[i] == "D":
                li.append(2*li[-1])
            elif operations[i] == "+":   
                 li.append(li[-1] +li[-2] )  
            else :
                li.append(int(operations[i]))       
        return sum(li)          
