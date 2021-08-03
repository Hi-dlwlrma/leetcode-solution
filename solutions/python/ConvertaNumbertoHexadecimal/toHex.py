class Solution:
    def toHex(self, num: int) -> str:
        def negativeNum(x): # two's complement
            # binary form
            bin_arr = list(bin(x)[2:])

            # invert the digits 0 becomes 1, 1 becomes 0
            for i in range(len(bin_arr)):
                if bin_arr[i] == "0":
                    bin_arr[i] = "1"
                else:
                    bin_arr[i] = "0"

            # add one
            bin_str = "0b" + "".join(bin_arr)
            num = int(bin_str, 2) + 1 # add one
            
            bin_str = bin(num)[2:]
            s = "".join(["0"]*(len(bin_arr) - len(bin_str))) + bin_str

            res = "0b" + "".join(["1"]*(32 - len(s))) + s
            return hex(int(res, 2))[2:]
        
        
        
        return negativeNum(-num) if num < 0 else hex(num)[2:]
      
#         if num == 0:
#             return "0"
#         result = ""
#         values = "0123456789abcdef"
#         if num < 0:
#             num = num + (2 ** 32)
#         while num > 0:
#             result = values[num % 16] + result
#             num = num // 16
#         return result
