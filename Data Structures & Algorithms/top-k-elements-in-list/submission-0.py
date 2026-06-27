class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in nums:
            if freq.get(i):
                freq[i]+=1
            else :
                freq[i]=1
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return  [key for key, value in sorted_freq[:k]]
        

        