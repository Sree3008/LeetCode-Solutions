class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        list=[]
        for i in nums:
            if i==2:
                list.append(-1)
                continue
            x=i
            bit=0
            while(i>>bit)&1:
                bit+=1
            x=i^(1<<(bit-1))
            list.append(x)
        return list

