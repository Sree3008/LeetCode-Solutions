class Solution:
    def findDelayedArrivalTime(self, a: int, d: int) -> int:
        x=a+d
        if x==24:
            return 0
        elif x<24:
            return x
        else:
            y=x-24
            return y
