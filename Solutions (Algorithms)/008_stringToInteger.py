class Solution:
    def myAtoi(self, s: str) -> int:
        x = s.strip()
        
        if x == '':
            return 0
        
        result = ''
        if x[0] in ['-', '+']:
            result = x[0]
            x = x[1:]
        
        for i in x:
            if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                result = result + i
            else:
                break
                
        if result in ['', '-', '+']:
            return 0
            
        if int(result) < -2**31:
            result = -2**31
        if int(result) > 2**31-1:
            result = 2**31-1
        
        return int(result)
