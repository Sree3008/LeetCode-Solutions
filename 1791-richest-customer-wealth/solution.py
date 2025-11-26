class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
       
        list1=[]
        for i in accounts:
            sum=0
            for j in i:
                sum=sum+j
            list1.append(sum)
        return max(list1)
            
        
