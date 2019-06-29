class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for j in t:
            if j in d:
                d[j] -= 1
            else:
                d[j] = 1
        for k,i in d.items():
            if i != 0:
                return False
        return True 
        