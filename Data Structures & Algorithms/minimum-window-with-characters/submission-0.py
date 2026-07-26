from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = Counter(t)
        have = {}
        required = len(need)
        formed = 0

        left = 0
        min_len = float("inf")
        start = 0

        for right in range(len(s)):
            c = s[right]
            have[c] = have.get(c, 0) + 1

            if c in need and have[c] == need[c]:
                formed += 1

            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                left_char = s[left]
                have[left_char] -= 1

                if left_char in need and have[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        return "" if min_len == float("inf") else s[start:start + min_len]