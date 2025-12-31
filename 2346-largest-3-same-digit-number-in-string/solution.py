class Solution:
    def largestGoodInteger(self, num: str) -> str:
        list1=list(num)
        list2=[]
        for i in range(1,len(list1)-1):
            if list1[i]==list1[i-1] and list1[i]==list1[i+1]:
                list2.append(list1[i]*3)
        if list2:
            return max(list2)
        return ""

