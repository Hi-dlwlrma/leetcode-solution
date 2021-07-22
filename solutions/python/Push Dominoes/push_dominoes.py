class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        arr = [i for i in range(len(dominoes)) if dominoes[i] != '.']
        if arr == []:
            return dominoes
        
        res = ''
        
        for i in range(len(arr)):
            if i == 0:
                if arr[i] != 0:
                    if dominoes[arr[i]] == 'L':
                        res += ''.ljust(arr[i], 'L')
                    else:
                        res += dominoes[:arr[i]]
                        
            else:
                fi = dominoes[arr[i-1]]
                se = dominoes[arr[i]]
                if fi == se:
                    res += ''.ljust(arr[i]-arr[i-1], fi)
                elif fi == 'R' and se == 'L':
                    if (arr[i]-arr[i-1]) % 2 != 0:
                        n = int((arr[i]-arr[i-1]+1)/2)
                        res += ''.ljust(n, 'R') + ''.ljust(n-1, 'L')
                    else:
                        n = int((arr[i]-arr[i-1])/2)
                        res += ''.ljust(n, 'R') + '.' + ''.ljust(n-1, 'L')
                else:
                    res += dominoes[arr[i-1]:arr[i]]
                    
            if i == len(arr)-1:
                res += dominoes[arr[i]]
                if arr[i] < len(dominoes)-1:
                    if dominoes[arr[i]] == 'R':
                        res += ''.ljust(len(dominoes)-1-arr[i], 'R')
                    else:
                        res += dominoes[arr[i]+1:]
        
        return res
