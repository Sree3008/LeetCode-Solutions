class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        list1=[]
        for i in range(0,len(s),k):
            list1.append(s[i:i+k])
        list2=[]
        for i in range(len(list1)):
            if len(list1[i])!=k:
                x= k-len(list1[i])
                list1[i]=list1[i]+fill*x
        print(list1)
        return list1
        
        


