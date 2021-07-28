class Solution:
    def countPrimes(self, n: int) -> int:
        # prime: so nguyen to
        if n <= 1:
            return 0
        
        count = [1] * n
        
        for i in range(2, n):
            if i*i >= n: # square
                break
            if count[i] == 0:
                continue
            for j in range(i*i, n, i):
                count[j] = 0
        return sum(count[2:n])
