class Solution:
    def maxProduct(self, n: int) -> int:
        s=str(n)
        list1=[]
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                list1.append(int(s[i])*int(s[j]))
        return max(list1)

