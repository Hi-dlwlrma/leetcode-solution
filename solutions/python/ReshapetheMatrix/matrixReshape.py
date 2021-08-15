class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # M[i][j]=M[n*i+j] , where n is the number of cols
        # M[i] => M[i/n][i%n]
        
        m, n = len(mat), len(mat[0])
        if r*c != m*n:
            return mat
        
        arr = [mat[i][j] for i in range(m) for j in range(n)]
        res = [[0 for j in range(c)] for i in range(r)] 
        for i in range(len(arr)):
            res[i//c][i%c] = arr[i]
        return res
