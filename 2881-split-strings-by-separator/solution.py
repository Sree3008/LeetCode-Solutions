class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        list1=[]
        for i in words:
            for j in i.split(separator):
                if j!='':
                    list1.append(j)
        return list1

