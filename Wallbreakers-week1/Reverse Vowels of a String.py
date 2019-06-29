class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels='aeiouAEIOU'
        vow=[i for i,j in enumerate(s) if j in vowels]
        vowrev =list(s)
        i,j=0,len(vow)-1
        while i<j:
            vowrev[vow[i]],vowrev[vow[j]]= vowrev[vow[j]], vowrev[vow[i]]
            i+=1
            j-=1
        return ''.join(vowrev)
           