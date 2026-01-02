class Solution:
    def countBits(self, n: int) -> List[int]:
        list1=[]
        for i in range(0,n+1):
            list1.append(str(bin(i)))
        list2=[]
        for i in list1:
            c=0
            for j in i:
                if j=='1':
                    c+=1
            list2.append(c)
        return list2


