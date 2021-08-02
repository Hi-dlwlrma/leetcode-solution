class Solution:
    def countBits(self, n: int) -> List[int]:
        # solution 1
        # res = []
        # for i in range(n+1):
        #     s = bin(i)[2:]
        #     res.append(sum([int(i) for i in s]))
        # return res
        
        # solution 2: generate new range from previous
        res = [0]
        
        while len(res) < n+1:
            temp = []
            for i in res:
                temp.append(i+1)
            res += temp
        return res[:n+1]
