class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        list1=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j or j==len(nums)-i-1:
                    list1.append(nums[i][j])
        print(list1)
        list2=[]
        for i in list1:
            if i>1:
                c=0
                for j in range(2, int(i**0.5)+1):
                    if i%j==0:
                        c+=1
                        break
                if c==0:
                    list2.append(i)
        if list2:
            return max(list2)
        return 0

