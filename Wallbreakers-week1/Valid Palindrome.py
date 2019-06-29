class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = []
        for i in s:
            if i.isalnum():
                l.append(i.lower())
        r = l[::-1]
        result1 = "".join(l)
        
        result2 = "".join(r)
        
        if result1 == result2:
            return True
        return False 
        