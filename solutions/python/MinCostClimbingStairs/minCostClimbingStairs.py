class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cost.append(0)
        
        f = [cost[0], cost[1]]
        
        for i in range(2, len(cost)):
            f.append(cost[i] + min(f[i-1], f[i-2]))
            
        return f[-1]
