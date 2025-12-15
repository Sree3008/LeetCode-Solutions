class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        list1=[]
        for i in tasks:
            s=0
            for j in i:
                s=s+j
            list1.append(s)
        return min(list1)

