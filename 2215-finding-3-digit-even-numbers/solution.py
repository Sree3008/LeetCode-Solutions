class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res=set()
        n=len(digits)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i==j or j==k or k==i:
                        continue
                    ans=digits[i]*100+digits[j]*10+digits[k]
                    if digits[i]!=0 and ans%2==0:
                        res.add(ans)
        list1=list(res)
        list1.sort()
        return list1
                
        
