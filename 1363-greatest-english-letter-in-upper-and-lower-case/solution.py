class Solution:
    def greatestLetter(self, s: str) -> str:
        list=[]
        for i in s:
            list.append(i)
        for j in sorted(list,reverse=True):
            if j.isupper():
                if j.lower() in list:
                    return j
        return ""
