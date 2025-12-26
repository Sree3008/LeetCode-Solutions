class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        list1=[]
        for i in words:
            for j in words:
                if i in j and i!=j:
                    list1.append(i)
                    break
        return list1
