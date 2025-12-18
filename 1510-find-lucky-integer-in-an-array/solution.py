class Solution:
    def findLucky(self, arr: List[int]) -> int:
        x=Counter(arr)
        list1=[]
        print(x)
        for i,v in x.items():
            if(i==v):
                list1.append(i)
        if list1:
            return max(list1)
        return -1
        
