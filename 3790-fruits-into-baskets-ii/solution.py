class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        c=0
        for i in range(len(fruits)):
            b=False
            for j in range(len(baskets)):
                if fruits[i]<=baskets[j]:
                    b=True 
                    baskets.pop(j)
                    break
            if not b:
                c+=1
        return c 
        
