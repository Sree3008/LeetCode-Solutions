class Solution:
    def frequencySort(self, s: str) -> str:
        arr=[]
        for x,y in Counter(s).items():
            arr.append(((-y),x))
        heapq.heapify(arr)
        res=''
        while arr:
            y,x=heapq.heappop(arr)
            res=res+x*(-y)
        return res
        
        
        
