from collections import Counter
class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        list1=[]
        X=Counter(bulbs)
        for i,v in X.items():
            if v%2==1:
                list1.append(i)
        return sorted(list1)
                
