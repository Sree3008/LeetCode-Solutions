class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        list1=[]
        
        for i in nums1:
            b=True
            s=nums2.index(i)
            for j in range(s+1,len(nums2)):
                if i<nums2[j]:
                    b=False
                    list1.append(nums2[j])
                    break
            if b:
                list1.append(-1)
        return list1
