class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        count=sum(apple)
        capacity.sort()
        capacity.reverse()
        c=0
        for i in capacity:
            count-=i
            c+=1
            if count<=0:
                return c

