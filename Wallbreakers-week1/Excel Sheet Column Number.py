class Solution:
    def titleToNumber(self, s: str) -> int:
        temp = 0
        for item in range(0,len(s)):
            temp = temp*26 + ((ord(s[item])-ord('A'))+1)
        return temp 
            
        