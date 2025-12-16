class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        list1=[]
        x=text.split()
        for i in x:
            c=0
            for j in i:
                if j in brokenLetters:
                    c=1
                    break
            if c==0:
                list1.append(i)
        return len(list1)


        
