class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        # formula: 0.5*abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)))
        # cuemath.com/geometry/area-of-triangle-in-coordinate-geometry/
        
        n = len(points) # row 
        m = len(points[0]) # col
        
        res = []
        
        for i in range(n):
            (x1, y1) = (points[i][0], points[i][1])
            for j in range(1, n):
                (x2, y2) = (points[j][0], points[j][1])
                for k in range(2, n):
                    x3, y3 = (points[k][0], points[k][1])
                    res.append(0.5*abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))))
        
        return max(res)

            
