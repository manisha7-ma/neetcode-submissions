class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sort1=sorted(s)
        sort2=sorted(t)
        if sort1==sort2:
            return True
        else:
            return False