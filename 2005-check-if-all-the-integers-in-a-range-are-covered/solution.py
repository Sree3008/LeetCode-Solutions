class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        list1=set()
        for i in ranges:
            for j in range(i[0],i[1]+1):
                list1.add(j)
        list2=list(list1)
        list3=[]
        for i in range(left,right+1):
            list3.append(i)
        for i in list3:
            if i not in list2:
                return False
        return True

        
