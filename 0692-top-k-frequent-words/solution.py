class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        arr=[]
        for x,y in Counter(words).items():
            arr.append(((-y),x))
        heapq.heapify(arr)
        res=[]
        # while k!=0:
        #     k=k-1
        for i in range(k):
            x,y=heapq.heappop(arr)
            res.append(y)
        return res
        


