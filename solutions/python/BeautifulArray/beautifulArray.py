class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        # even + even = 2k (i<k<j)
        # odd + odd = 2k (i<k<j)
        # => odd even odd even odd (eg. 1 2 3 4 5)
        # => these two cases are not allowed
        # therefore, we have a case are allowed: odd odd even even (eg. 1 3 5 2 4)
        # BUT it won't work because 1 + 5 = 2 * 3
        # => we have to sort odd elements and even elements
        # * odd elements: 2x-1 (x = 1)
        # * even elements: 2x (x = 1)
        # if we start from beautiful array, we'll create a new beautiful array
        # with above fomular, then adding odd array and even array to finish
        # eg.
        # beautiful_arr = [2, 1, 4, 3]
        # odd_arr       = ([2, 1, 4, 3] * 2 - 1) = [3, 1, 7, 5]
        # even_arr      = ([2, 1, 4, 3] * 2)     = [4, 2, 8, 6]
        # => Result:
        # new_beautiful_arr = odd_arr + even_arr
        #                   = [3, 1, 7, 5, 4, 2, 8, 6]
        
        beautiful_arr = [1]
        
        while len(beautiful_arr) < n:
            odd_arr = [2*i - 1 for i in beautiful_arr]
            even_arr = [2*i for i in beautiful_arr]
            beautiful_arr = odd_arr + even_arr
        
        return [i for i in beautiful_arr if i <= n]
