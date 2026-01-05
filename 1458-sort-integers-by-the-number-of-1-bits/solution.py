class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        list1=[]
        for i in arr:
            x=bin(i)
            c=0
            for j in x:
                if j=='1':
                    c+=1
            list1.append(c)
        list2=[]
        for i,v in zip(list1,arr):
            list2.append([i,v])
        list2.sort()
        list3=[]
        for i in list2:
            list3.append(i[1])
        return list3


        
