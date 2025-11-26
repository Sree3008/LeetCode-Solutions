class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''
        for i in digits:
            s=s+str(i)
        res=int(s)+1
        st=str(res)
        list1=[]
        while res!=0:
            m=res%10
            list1.append(m)
            res=res//10
        return list1[::-1]
