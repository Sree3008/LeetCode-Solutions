class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        list1=set(nums1)
        num1=list(list1)
        list2=set(nums2)
        num2=list(list2)
        list3=set(nums3)
        num3=list(list3)
        num1.extend(num2)
        num1.extend(num3)
        x=Counter(num1)
        print(x)
        res=[]
        for i,v in x.items():
            if v>1:
                res.append(i)
        res[::-1]
        return res
