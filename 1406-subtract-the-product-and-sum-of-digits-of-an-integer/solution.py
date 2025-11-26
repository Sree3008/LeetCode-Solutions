class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mul=1
        sum=0
        while n!=0:
            m=n%10
            sum=sum+m
            mul=mul*m
            n=n//10
        print(sum)
        print(mul)
        return mul-sum
