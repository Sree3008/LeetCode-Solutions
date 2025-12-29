class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s=str(x)
        list1=list(s)
        sum1=0
        for i in list1:
            sum1+=int(i)
        if x%sum1==0:
            return sum1
        return -1

