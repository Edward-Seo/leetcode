class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        y_str = x_str
        y_str = y_str[::-1]
        if x_str == y_str:
            return True
        else:
            return False
