class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        r_m=[min(row) for row in matrix]
        c_m=[max(col) for col in zip(*matrix)]
        s1=set(r_m)
        s2=set(c_m)
        s3=s1.intersection(s2)
       
        return list(s3)
