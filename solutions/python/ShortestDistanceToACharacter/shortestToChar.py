class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        
        # find char
        pos = [index for index, char in enumerate(s) if char == c]
        
        # initialize
        ans = []
        j = 1
        left = pos[0]
        right = pos[j] if j < len(pos) else -1
        
        # main code
        for i in range(len(s)):
            
            if i <= left or i > right:
                ans.append(abs(i-left))
                
            elif i > left and i < right:
                ans.append(min(abs(i-left), abs(i-right)))
                
            elif i == right:
                ans.append(0)
                left = right
                j = j+1
                if j < len(pos):
                    right = pos[j]
                
        return ans
        
       
