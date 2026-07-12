class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        l = [0] * (2*n)
        for i in range(n):
            l[i] = nums[i]
            l[i+n] = nums[i]
        return l
        
