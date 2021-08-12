class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        # from collections import Counter
        count = collections.Counter(arr)
        # Counter({'x': 4, 'y': 2, 'z': 2})
        for x in sorted(arr, key=abs): # [-2, 2, 4, -4]
            if count[x] == 0: continue
            if count[2*x] == 0: return False
            count[x] -= 1
            count[2*x] -= 1

        return True
