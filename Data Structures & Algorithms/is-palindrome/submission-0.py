class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        s="".join(ch for ch in s if ch.isalnum()).lower()
        j=len(s)-1
        while i<j:
            if s[i]!=s[j]:
                #print(s[i],"%",s[j])
                return False
                break
            i+=1
            j-=1
        return True