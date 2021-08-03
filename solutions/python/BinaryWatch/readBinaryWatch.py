class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
    
        res = []
        
        def countBit(num):
            s = bin(num)[2:]
            s = [int(i) for i in s]
            return sum(s)
        def convert(hour, minute=0):
            if minute < 10:
                txt = "{hour}:0{minute}"
            else:
                txt = "{hour}:{minute}"
            return txt.format(hour = hour, minute = minute)
        
        # main function
        if turnedOn > 8:
            return res
        
        for i in range(0, 12):
            x = countBit(i)
            # print(x)
            if x == turnedOn:
                res.append(convert(i))
            elif x < turnedOn:
                target = turnedOn - x
                for j in range(1, 60):
                    y = countBit(j)
                    if y == target:
                        res.append(convert(i, j))
        return res
