class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''
        for i in digits:
            s=s+str(i)
        x=int(s)+1
        return [int(i) for i in str(x)]
