class Solution:
    def isValid(self, s: str) -> bool:
        count = 0
        while count == 0:
            a = s
            s = s.replace("()",'')
            s = s.replace("{}",'')
            s = s.replace("[]",'')
            if a == s:
                count = 1
        if len(s) == 0:
            return True
        else:
            return False
