class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        import numpy as np
                    
        mat = np.array(mat)
        rows = mat.shape[0]
        cols = mat.shape[1]
        
        for i in range(rows):
            for j in range(cols):
                if mat[i,j] > 0:
                    left, top = 100000, 100000
                    if i > 0:
                        left = mat[i-1,j] + 1
                    if j > 0:
                        top = mat[i,j-1] + 1
                    mat[i,j] = min(left,top)
                    
        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                if mat[i,j] > 0:
                    if i < rows-1:
                        mat[i,j] = min(mat[i,j], mat[i+1,j] + 1)
                    if j < cols-1:
                        mat[i,j] = min(mat[i,j], mat[i,j+1] + 1)
        return mat
