class Solution:
    def maxPoints(self, tec1: List[int], tec2: List[int], k: int) -> int:
        n=len(tec1)
        task=[]
        for i in range(n):
            diff=tec1[i]-tec2[i]
            task.append((diff,tec1[i],tec2[i]))
        task.sort(reverse=True)
        total=0
        for i in range(k):
            total+=task[i][1]
        for i in range(k,n):
            total+=max(task[i][1],task[i][2])
        return total
