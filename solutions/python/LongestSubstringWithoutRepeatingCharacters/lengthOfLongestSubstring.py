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
    
#         solution 2
#         temp = ''   # chuoi temp
#         longest, lmax = 0, 0
        
#         for i in range(len(s)):
            
#             if s[i] not in temp:
#                 longest += 1 # neu khong trung
#                 if longest > lmax:
#                     lmax = longest
#                 temp += s[i] # them vao chuoi temp ky tu khong trung

#             else:
#                 pos = temp.index(s[i]) + 1 # vi tri ky tu bi trung
#                 longest = longest - pos + 1 # neu trung
#                 if longest > lmax:
#                     lmax = longest
#                 temp = temp[pos:] + s[i] # temp = bo ky tu trung + ky tu moi
                
#         return lmax
