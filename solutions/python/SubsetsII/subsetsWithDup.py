class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def getSubset(i, elem, res):
            if i == len(nums):
                return
            for j in range(i, len(nums)):
                elem.append(nums[j])
                if elem.copy() not in res:
                    res.append(elem.copy())
                getSubset(j+1, elem, res)
                elem.pop()
                
        
        nums.sort()
        elem, res = [], []
        res.append([])
        getSubset(0, elem, res)

        return res
