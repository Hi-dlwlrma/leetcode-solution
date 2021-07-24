class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        def countString(s):
            for i in s:
                if (s.count(i) > 1):
                    return False
            return True
        
        split = lambda s,n: [(s[i:i+n]) for i in range(len(s)) if i+n <= len(s)]
        
        for i in range(len(set(s)), 0, -1):
            s_n_char = split(s, i)
            for j in s_n_char:
                if countString(j):
                    return i
                
        return 0
