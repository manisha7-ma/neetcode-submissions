class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i,j,mx=0,1,0
        while i<j:
            buy=prices[i]
            j=i+1
            while j<len(prices):
                if mx<(prices[j]-buy):
                    mx=prices[j]-buy
                j+=1
            i+=1
        return mx


        