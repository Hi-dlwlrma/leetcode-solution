class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
#         mid = len(arr) // 2
        
#         if arr[mid-1] < arr[mid]: # implement right side
#             for i in range(mid, len(arr)-1):
#                 if arr[i] > arr[i+1]:
#                     return i
                
#         if arr[mid] > arr[mid+1]: # implement left side
#             for i in range(mid, 0, -1):
#                 if arr[i] > arr[i-1]:
#                     return i
                
        left = 0
        right = len(arr)-1
        
        while left < right:
            mid = (left+right)//2
            if arr[mid] < arr[mid+1]:
                left = mid+1
            else:
                right = mid
        return left
                
