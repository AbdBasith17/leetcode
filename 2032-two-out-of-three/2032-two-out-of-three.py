class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        res = set(nums1 + nums2+ nums3)
        l = []
        for i in res:
   
            if i in nums1 and i in  nums2 :
                l.append(i)
            elif i in  nums2 and  i in nums3 :
                l.append(i)
            elif i in nums1 and i in  nums3:
                l.append(i)
        return l