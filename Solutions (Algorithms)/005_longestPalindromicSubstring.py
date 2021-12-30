class Solution:
    def longestPalindrome(self, s: str) -> str:
        str_s = s
        result_list = []
        
        while len(str_s) > 0:
            an = ''
            for i in str_s:
                an = an + i
                if an == an[::-1]:
                    result_list.append(an)
            str_s = str_s[1:]
        
        result_length = 0
        result = ''
        
        for i in result_list:
            if len(i) > result_length:
                result_length = len(i)
                result = i
                
        return result
