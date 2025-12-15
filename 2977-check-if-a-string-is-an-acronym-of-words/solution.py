class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        list1=[]
        for i in words:
            list1.append(i[0])
        print(list1)
        st=''
        for i in list1:
            st+=i
        return st==s

        
