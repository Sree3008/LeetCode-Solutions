class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        list1=target[0]
        for i in range(1,len(target)):
            if target[i]>target[i-1]:
                list1+=target[i]-target[i-1]
        return list1
        
