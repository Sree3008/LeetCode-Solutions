class Solution:
    def reformat(self, s: str) -> str:
        list1=[]
        list2=[]
        for i in s:
            if i.isdigit():
                list1.append(i)
            else:
                list2.append(i)
        if abs(len(list1) - len(list2)) > 1:
            return ""
        if len(list2) > len(list1):
            list1, list2 = list2, list1
        st=''
        for i in range(len(list2)):
                st+=list1[i]
                st+=list2[i]
        if len(list1)>len(list2):
            st+=list1[-1]
        return st

        
