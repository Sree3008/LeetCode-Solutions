class Solution:
    def secondHighest(self, s: str) -> int:
        list1=[]
        for i in s:
            if i.isdigit():
                list1.append(int(i))
        list2=set(list1)
        print(list2)
        if len(list2)<2:
            return -1
        y=list(list2)
        y.sort(reverse=True)
        return y[1]   
