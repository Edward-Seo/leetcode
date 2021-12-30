class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x)
        
        if x < 0:
            str_x = str_x[1:]
            
        str_rev_x = str_x[::-1]
        
        int_rev_x = int(str_rev_x)
        
        if x < 0:
            int_rev_x = int_rev_x * (-1)
            
        if int_rev_x not in range(-(2**31), 2**31):
            return 0
        
        return int_rev_x
