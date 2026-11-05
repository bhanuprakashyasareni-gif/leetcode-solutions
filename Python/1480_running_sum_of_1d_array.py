class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        x = []
        l = 0 
        for i in nums:
            l += i
            x.append(l)
        return x

s = Solution()
print(s.runningSum([1,2,3,4]))
