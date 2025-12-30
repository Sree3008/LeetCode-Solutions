class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        list1=[]
        for i in responses:
            list2=set()
            for j in i:
                list2.add(j)
            list1.append(list(list2))
        list3=[]
        for i in list1:
            for j in i:
                list3.append(j)
        x=Counter(list3)
        maxi=max(x.values())
        res=[]
        for i,v in x.items():
            if v==maxi:
                res.append(i)
        return min(res)

