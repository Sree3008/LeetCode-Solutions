class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        s=set()
        n=len(digits)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i==j or j==k or k==i:
                        continue
                    res=digits[i]*100+digits[j]*10+digits[k]
                    if digits[i]!=0 and res%2==0:
                        s.add(res)
        return len(s)
