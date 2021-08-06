class Solution:
    def arrangeCoins(self, n: int) -> int:
        # staircase: cau thang bo
        
        # coin = [0, 1]
        # i = 1
        # while coin[i] <= n:
        #     coin.append(coin[i] + i + 1)
        #     i += 1
        # return i-1
        
        # solution 2
        # 1 + 2 + . . . + k = (k(k+1)) // 2 coins
        
        left, right = 0, n
        while left <= right:
            step = (right + left) // 2
            coin = step*(step+1) // 2
            if coin == n:
                return step
            elif coin > n:
                right = step - 1
            else:
                left = step + 1
        return right
