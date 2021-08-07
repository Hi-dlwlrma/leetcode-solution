class Solution:
    def toHex(self, num: int) -> str:
        def findComplement(num):
            s = bin(num)[2:]
            res = ''
            for i in s:
                res += str(int(i) ^ 1) # xor 1^1=0 0^1=1
            res = '0b' + res
            return int(res, 2), len(res) - 2
        
        def convertHex(num):
            if num == 0:
                return "0"
            res = ""
            val = "0123456789abcdef"
            # if num < 0:
            #     num = num + (2 ** 32)
            while num > 0:
                res = val[num % 16] + res
                num = num // 16
            return res

        def negativeNum(x):
            num, length = findComplement(x) 
            num += 1 # add one
            s = "{:032b}".format(num)
            res = "0b" + "".join(["1"]*(32 - length)) + s[-length:]
            return convertHex(int(res, 2))
        
        return negativeNum(-num) if num < 0 else convertHex(num)
