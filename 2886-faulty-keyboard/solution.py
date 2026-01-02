class Solution:
    def finalString(self, s: str) -> str:
        list1=list(s)
        list2=[]
        for j in list1:
            if j!='i':
                list2.append(j)
            else:
                list2.reverse()
        return ''.join(list2)
