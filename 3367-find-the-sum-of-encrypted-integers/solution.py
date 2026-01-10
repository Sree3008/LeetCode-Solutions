class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        list1=[]
        list2=[]
        for i in nums:
            if len(str(i))==1:
                list1.append(i)
            else:
                maxi=0
                x=str(i)
                for j in x:
                    maxi=max(maxi,int(j))
                list2.append([maxi]*len(x))
        list3=[]
        for i in list2:
            s=''
            for j in i:
                s+=str(j)
            list3.append(int(s))
        return sum(list3)+sum(list1) 

