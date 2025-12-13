class Solution:
    def countConsistentStrings(self, nums1: str, nums2: List[str]) -> int:
        
        x=0
        for i in nums2:
            c=True
            for j in i:
                if j not in nums1:
                    c=False
                    break
            if c:
                x+=1
        return x
        

