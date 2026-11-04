class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l , r = 0 , len(nums)-1
        last = 0 
        m = 0
        while l <= r :
            m = l + (r-l)//2
            if nums[m] == target :
                return m
            else:
                if nums[m] < target:
                    l = m + 1
                    last = l
                else:
                    r = m - 1
                    last = r
        if nums[m] <= target :
            return m + 1


        return m

o = Solution()
print(o.searchInsert([1,2,3,5,6,9],8))
                

        
