class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        list1=[]
        for i in range(len(mat)):
            c=0
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    c+=1
            list1.append(c)
        list2=[]
        for i,v in enumerate(list1):
            list2.append((i,v))
        list2.sort(key=lambda x:x[1])
        list3=[]
        for i in list2[:k]:
            list3.append(i[0])
        return list3
        
        

        
        


