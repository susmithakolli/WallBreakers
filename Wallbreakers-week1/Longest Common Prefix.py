class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        l = min(strs)
        for i in range(len(l)):
            for j in strs:
                if j[i] != l[i]:
                    return l[:i] if i>0 else ""
        return l