class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # solution 1: Find substring
        count = 0
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                left, right = i, i+1
                while s[left] == s[i] and s[right] == s[i+1]:
                    left -= 1
                    right += 1
                    if left < 0 or right >= len(s):
                        break
                count += (right- left)//2
        return count
      
        # solution 2: Group by character
        res, x = 0, 0
        count = []
        s += '2'
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                count.append(i-x)
                x = i
        for i in range(len(count)-1):
            res += min(count[i], count[i+1])
        return res
