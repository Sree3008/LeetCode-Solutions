class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        r0,r1,r2=[],[],[]
        for x in nums:
            if x%3==0:
                r0.append(x)
            elif x%3==1:
                r1.append(x)
            else:
                r2.append(x)
        r0.sort(reverse=True)
        r1.sort(reverse=True)
        r2.sort(reverse=True)
        ans=0
        if len(r0)>=3:
            ans=max(ans,sum(r0[:3]))
        if len(r1)>=3:
            ans=max(ans,sum(r1[:3]))
        if len(r2)>=3:
            ans=max(ans,sum(r2[:3]))
        if r0 and r1 and r2:
            ans=max(ans,r0[0]+r1[0]+r2[0])
        return ans
