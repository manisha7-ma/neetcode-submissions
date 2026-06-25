class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for j, nums  in enumerate(nums):
            if target-nums in hashmap:
                return [hashmap[target-nums],j]
            else:
                hashmap[nums]=j
        
        