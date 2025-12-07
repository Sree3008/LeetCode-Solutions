class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        list1=[]
        for n in nums:
            b=bin(n)[2:]
            rev=b[::-1]
            ref=int(rev,2)
            list1.append((ref,n))
        list1.sort() 
        return [num for _,num in list1] 
            
