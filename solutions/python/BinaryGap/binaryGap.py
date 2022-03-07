class Solution:
    def binaryGap(self, n: int) -> int:
        s = bin(n)[2:]
        
        pos = [i for i in range(len(s)) if s[i] == '1']
        
        if len(pos) <= 1:
            return 0
        
        return max(pos[i+1] - pos[i] for i in range(len(pos)-1))
        
        # longest_distance = 0
        # for i in range(1, len(pos)):
        #     dist = pos[i] - pos[i-1] 
        #     if dist > longest_distance:
        #         longest_distance = dist
        # return longest_distance
