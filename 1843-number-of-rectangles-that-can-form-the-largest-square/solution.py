class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        list1=[]
        for i in rectangles:
            list1.append(min(i[0],i[1]))
        x=max(list1)
        return list1.count(x)
