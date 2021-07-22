class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ret = 0
        nums.sort()
        
        for i in range(2, len(nums)):
            a = 0
            b = i-1
            while a < b:
                if nums[a] + nums[b] > nums[i]:
                    ret += (b - a)
                    b -= 1
                else:
                    a += 1
        return ret
        
