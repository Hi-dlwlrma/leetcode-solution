class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # legibility: tinh de doc
        if numRows == 1:
            return s
        
        res = ""
        v_line = numRows + numRows - 2
        
        # solution 1
        # add v line
        half_v_line = len(s) % v_line
        if half_v_line < v_line:
            s += ''.ljust(v_line - half_v_line)
        
        # add last column
        last_col = len(s) % v_line
        s += ''.ljust(numRows - last_col)
        
        for i in range(numRows):
            for j in range(i, len(s), v_line):
                if i > 0 and i < numRows-1:
                    between = j - i * 2
                    if between > 0 and numRows > 2:
                        res += s[between] + s[j]
                        continue
                res += s[j]
        return res.replace(' ', '')

#         solution 2
#         for i in range(numRows):
#             for j in range(0, len(s)-i, v_line):
#                 res += s[j + i]
#                 if i != 0 and i != numRows-1 and j + v_line - i < len(s):
#                     res += s[j + v_line - i]
                    
#         return res
