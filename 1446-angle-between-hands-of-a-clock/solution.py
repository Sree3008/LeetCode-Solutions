class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        res=(hour%12)*30+minutes*0.5
        res1=minutes*6
        res3=abs(res-res1)
        return min(res3,360-res3)
        
