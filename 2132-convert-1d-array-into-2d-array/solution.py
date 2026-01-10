import numpy as np
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        arr=np.array(original)
        arr2=arr.reshape(m,n) 
        return arr2.tolist()
        
