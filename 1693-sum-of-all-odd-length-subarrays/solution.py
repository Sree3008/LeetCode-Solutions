class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        list1=[]
        for i in range(len(arr)):
            for j in range(i+1,len(arr)+1):
                list1.append(arr[i:j])
        c=0
        for i in range(0,len(list1)):
            if len(list1[i])%2!=0:
                c+=sum(list1[i])
        return c
