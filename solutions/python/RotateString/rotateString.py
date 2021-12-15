class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        from collections import Counter
        mydist = Counter(list(s))
        for c in goal:
            if mydist[c] != goal.count(c):
                return False
            
        return True if goal in s+s else False
            
        
#         mid = len(s) // 2
        
#         left = s[:mid]
#         right = goal[mid:]
        
#         for letter in right:
#             if letter in left:
#                 return True
#         return False
