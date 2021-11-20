class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3 or nums == None:
            return False
        i = float("inf")
        j = float("inf")
        k = float("inf")
        
        for num in nums:
            if num <= i:
                i = num
            elif num <= j:
                j = num
            elif num <= k:
                k = num
        
        return (k < float("inf")) 
        