class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
         
        x1_rec1 = rec1[0]
        y1_rec1 = rec1[1]
        x2_rec1 = rec1[2]
        y2_rec1 = rec1[3]
        
        x1_rec2 = rec2[0]
        y1_rec2 = rec2[1]
        x2_rec2 = rec2[2]
        y2_rec2 = rec2[3]
        
        # compute intersection
        x1 = max(x1_rec1, x1_rec2)
        y1 = max(y1_rec1, y1_rec2)
        x2 = min(x2_rec1, x2_rec2)
        y2 = min(y2_rec1, y2_rec2)
        
        
        return (x2 > x1) and (y2 > y1)
        
        # area = (x2-x1) * (y2-y1)
