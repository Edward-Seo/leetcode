class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        an = ''
        substring_list = []

        range_int = len(s)
        str_s = s

        an = ''
        while len(str_s) > 0:
            for i in range(len(str_s)):
                if str_s[i] not in an:
                    an = an + str_s[i]
                else:
                    substring_list.append(an)
                    an = ''
                    str_s = str_s[1:]
                    break

        result = 0
        for i in substring_list:
            if len(i) > result:
                result = len(i)

        return result
