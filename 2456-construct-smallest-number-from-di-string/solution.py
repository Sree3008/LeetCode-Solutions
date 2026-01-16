class Solution:
    def smallestNumber(self, pattern: str) -> str:
        list1=[]
        res=''
        for i in range(len(pattern)+1): 
            list1.append(i+1)
            if i==len(pattern) or pattern[i]=='I':
                while list1:
                    res+=str(list1.pop())
        return res


