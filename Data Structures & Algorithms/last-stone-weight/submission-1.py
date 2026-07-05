class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        ret =0
        i,j=0,1
        while i<len(stones)-1:
            ele1=stones[i]
            ele2=stones[j]
            if ele1==ele2:
                ret=0
            elif ele1>ele2:
                ret=ele1-ele2
            else:
                ret=ele2-ele1
            stones=stones[j+1:len(stones)]
            stones.append(ret)
            stones.sort(reverse=True)
            #print(stones)
        return stones[0]

        