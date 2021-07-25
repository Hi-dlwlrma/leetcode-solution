class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expandAroundCenter(s, left, right):
            l, r = left, right
            while l >=0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1 # length of substring
        
        start, end = 0, 0
        for i in range(len(s)):
            len1 = expandAroundCenter(s, i, i)   # odd string
            len2 = expandAroundCenter(s, i, i+1) # even string
            k = max(len1, len2) # longest length of substring
            if k > (end - start):
                start = i - int((k - 1)/2)
                end = i + int(k/2)
                
        return s[start:end+1]
