class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
      
        for ch in ransomNote:
            count_r = 0
            count_m = 0

            for c in ransomNote:
                if c == ch:
                    count_r += 1

            for c in magazine:
                if c == ch:
                    count_m += 1
        
            if count_r > count_m:
                return False
    
        return True

