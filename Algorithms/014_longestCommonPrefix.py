# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Solution
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str_len_list = []
        for i in strs:
            str_len_list.append(len(i))
        str_len_list.sort()
        shortest_str = str_len_list[0]
        
        result = ''
        
        for i in range(shortest_str):
            checking_list = []
            count = 0
            for ii in strs:
                if strs[0][i] == ii[i]:
                    count += 1
            if count == len(strs):
                result = result + strs[0][i]
            else:
                return result
                
        return result
