class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxi=0
        altitude=0
        for i in range(len(gain)):
            altitude += gain[i]
            maxi = max(maxi, altitude)
        
        return maxi
        
