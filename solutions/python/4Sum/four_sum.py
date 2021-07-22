class Solution(object):
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
     
        def twoSum(nums, target):
            res = []
            mydict = {nums[i]: i for i in range(len(nums))}
            for i in range(len(nums)):
                if target - nums[i] not in mydict or mydict[target - nums[i]] == i:
                    continue
                a = nums[i]
                b = nums[mydict[target - nums[i]]]
                if sorted([a,b]) not in res:
                    res.append(sorted([a,b]))
            return res
        
        def kSum(nums, target, k, list_k_numbers, res):
            if k < 2:
                return;

            if k == 2:
                list_two_numbers = twoSum(nums, target)
                for i in range(len(list_two_numbers)):
                    elem = list_two_numbers[i]
                    if elem:
                        list_k_numbers.append(elem[0])
                        list_k_numbers.append(elem[1])

                        temp = list(list_k_numbers)

                        list_k_numbers.pop()
                        list_k_numbers.pop()

                        if temp not in res:
                            res.append(temp)
                            
            else:
                for i in range(len(nums)-2):
                    list_k_numbers.append(nums[i])
                    kSum(nums[i+1:], target-nums[i], k-1, list_k_numbers, res)
                    list_k_numbers.pop()
                return res
            
        nums.sort()
        return kSum(nums, target, 4, list_k_numbers = [], res = [])
