class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        p=[]
        for i in range(len(nums)):
            if nums[i]>=0:
                p.append(nums[i])
        if not p:
            return nums
        k=k%len(p)
        p=p[k:]+p[:k]
        id=0
        for i in range(len(nums)):
            if nums[i]>=0:
                nums[i]=p[id]
                id+=1
        return nums
