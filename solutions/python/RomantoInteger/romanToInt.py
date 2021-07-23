class Solution:
    def romanToInt(self, s: str) -> int:
        
        mydict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        res, i = 0, 0
        
        while i < len(s):
            
            if i+1 < len(s):
                temp = mydict[s[i+1]] - mydict[s[i]]
                if (temp > 0) and (temp%4 == 0 or temp%9 == 0):
                    res += temp
                    i += 2
                    continue
            res += mydict[s[i]]
            i += 1
            
        return res
