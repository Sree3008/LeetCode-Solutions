class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        list=[]
        for i in zip(names,heights):
            list.append(i)
        list.sort(key=lambda x:x[1],reverse=True)

        return [i[0] for i in list]
