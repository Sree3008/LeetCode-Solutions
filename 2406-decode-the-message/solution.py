class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        m={}
        c=ord('a')
        for i in key:
            if i!=' ' and i not in m:
                m[i]=chr(c)
                c+=1
        res=[]
        for i in message:
            if i==' ':
                res.append(' ')
            else:
                res.append(m[i]) 
        return ''.join(res)

