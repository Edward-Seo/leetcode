class Solution:
    def romanToInt(self, s: str) -> int:
        string_list = [x for x in s]
        
        numbers_dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        
        for i, ii in enumerate(s):
            if ii == 'I':
                try:
                    if s[i+1] == 'V':
                        string_list[i] = 'IV'
                        string_list[i+1] = ''
                    if s[i+1] == 'X':
                        string_list[i] = 'IX'
                        string_list[i+1] = ''
                except:
                    pass
            if ii == 'X':
                try:
                    if s[i+1] == 'L':
                        string_list[i] = 'XL'
                        string_list[i+1] = ''
                    if s[i+1] == 'C':
                        string_list[i] = 'XC'
                        string_list[i+1] = ''
                except:
                    pass                        
            if ii == 'C':
                try:
                    if s[i+1] == 'D':
                        string_list[i] = 'CD'
                        string_list[i+1] = ''
                    if s[i+1] == 'M':
                        string_list[i] = 'CM'
                        string_list[i+1] = ''
                except:
                    pass
                
        while '' in string_list:
            string_list.remove('')

        result = 0
        for i in string_list:
            result = result + numbers_dic[i]

        return result
