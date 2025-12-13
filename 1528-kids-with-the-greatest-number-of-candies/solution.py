class Solution:
    def kidsWithCandies(self, candies: List[int], e: int) -> List[bool]:
        t=max(candies)
        list1=[]
        for i in candies:
            x=i+e
            if x>=t:
                list1.append(True)
            else:
                list1.append(False)
        return list1

