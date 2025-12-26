class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        list1=[]
        for i in nums:
            if i%2==0:
                list1.append(i)
        x=Counter(list1)
        if list1:
            y=max(x.values())
        else:
            y=0
        list2=[]
        for i,v in x.items():
            if v==y:
                list2.append(i)
        print(list2)
        if list2:
            return min(list2)
        return -1
