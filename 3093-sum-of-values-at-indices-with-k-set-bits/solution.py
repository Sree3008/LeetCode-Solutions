class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        list1=[]
        for i in range(len(nums)):
            list1.append(bin(i))
        print(list1)
        list2=[]
        for v,i in enumerate(list1):
            c=0
            for j in i:
                if j=='1':
                    c+=1
            if c==k: 
                list2.append(nums[v])
        return sum(list2)


