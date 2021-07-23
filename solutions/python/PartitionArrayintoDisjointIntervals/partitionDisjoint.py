class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        
        a = list([nums[0]]) # smallest possible size
        b = list(nums[1:])
        
        while max(a) > min(b): # condition: left <= right

            index_min_b = b.index(min(b))
            index_min_b += len(a)
            
            a = list(nums[:index_min_b+1])
            b = list(nums[index_min_b+1:])
     
        return len(a)
