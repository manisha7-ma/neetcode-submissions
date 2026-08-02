from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()   # Stores indices of elements in decreasing order of values
        ans = []

        for i in range(len(nums)):
            # Remove indices that are outside the current window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Remove all smaller (or equal) elements from the back
            # because they can never be the maximum in future windows
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            # Add current index
            dq.append(i)

            # Once the first window is formed, record the maximum
            if i >= k - 1:
                ans.append(nums[dq[0]])

        return ans