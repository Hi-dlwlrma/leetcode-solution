class LargerNumKey(str):
    def __lt__(a, b): # < decreasing other
        return a + b > b + a
    
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        s = "".join(sorted(map(str, nums), key=LargerNumKey))
        return "0" if s[0] == "0" else s
#         if int(s) == 0:
#             return "0"
#         else:
#             return s
