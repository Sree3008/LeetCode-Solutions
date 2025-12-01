class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        res=[]
        for i in gifts:
            res.append(-i)
        heapq.heapify(res)
        
        while k!=0:
            k=k-1
            lar = -heapq.heappop(res)
            x=int(math.sqrt(lar))
            heapq.heappush(res,-x)
        
        sum=0
        for i in res:
            sum=sum+(-i)
        return sum
        
            
            
        

