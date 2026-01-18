class Solution:
    def maxCapacity(self, costs: List[int], cap: List[int], b: int) -> int:
        a=[(costs[i],cap[i]) for i in range(len(costs))]
        a.sort()
        n=len(a)
        ans=0
        pre=[0]*n
        pre[0]=a[0][1]
        for i in range(1,n):
            pre[i]=max(pre[i-1],a[i][1])
        for i in range(n):
            c,v=a[i]
            if c<b:
                ans=max(ans,v)
            rem=b-c
            if rem<=0:
                continue
            j=bisect_left(a,(rem,))-1
            if j<0:
                continue
            if j>=i:
                if i>0:
                    ans=max(ans,v+pre[i-1])
            else:
                ans=max(ans,v+pre[j])
        return ans
