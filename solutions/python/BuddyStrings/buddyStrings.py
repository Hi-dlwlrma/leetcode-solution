class Solution:
    def swap(self, s, a, b):
        return s[:a] + s[b] + s[a+1:b] + s[a] + s[b+1:]
    
    def buddyStrings(self, s: str, goal: str) -> bool:
        from collections import Counter
        arr = []

        for i in range(len(s)):
            if s[i] != goal[i]:
                arr.append(i)
        
        if len(arr)%2 != 0:
            return False
        else:
            if len(arr) == 0:
                char_similar = [val for key, val in Counter(s).items()]
                return True if max(char_similar) >= 2 else False
                 
            return True if self.swap(s, arr[0], arr[1]) == goal else False
                
                
