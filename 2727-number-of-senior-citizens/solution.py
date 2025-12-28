class Solution:
    def countSeniors(self, details: List[str]) -> int:
        list1=[]
        c=0
        for i in details:
            list1.append(i[-4:-2])
        for i in list1:
            if 60<int(i):
                c+=1
        return c
