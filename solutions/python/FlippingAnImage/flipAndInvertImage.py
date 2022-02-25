class Solution:
    def invertBinary(self, number):
        return 1 if number == 0 else 0
        
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        ans = []
        
        for row in image:
    
            mid = int(len(row)/2)        
            left, right = [], []
            
            for j in range(mid):
                if row[j] == row[len(row)-1-j]:
                    left.append(self.invertBinary(row[j]))
                    right.append(self.invertBinary(row[j]))
                else:
                    left.append(row[j])
                    right.append(row[len(row)-1-j])
            
            if len(row)%2 != 0: 
                left.append(self.invertBinary(row[mid]))
            ans.append(left + right[::-1])
            
        return ans
            
            
