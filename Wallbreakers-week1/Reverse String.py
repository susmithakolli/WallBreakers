class Solution:
    def reverseString(self, s: List[str]) -> None:
        start = 0
        stop = len(s)-1
        while start<stop:
            s[start],s[stop] = s[stop], s[start]
            start += 1
            stop -= 1