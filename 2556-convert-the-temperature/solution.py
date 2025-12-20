class Solution:
    def convertTemperature(self, cel: float) -> List[float]:
        return [cel+273.15,cel * 1.80 + 32.00]

        
