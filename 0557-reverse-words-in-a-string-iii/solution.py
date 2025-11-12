class Solution:
    def reverseWords(self, s: str) -> str:
        st=s.split(' ')
        list=[]
        for i in st:
            list.append(i[::-1])
        return " ".join(list)
