class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        x=set(word)
        y='qwertyuioplkjhgfdsazxcvbnm'
        z='QWERTYUIOPLKJHGFDSAZXCVBNM'
        a=[]
        b=[]
        c=0
        for i in x:
            if i in y:
                a.append(i)
            else:
                b.append(i)
        for i in a:
            if i.upper() in b:
                c+=1
        return c

        
