class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        x=0
        y=len(salary)-2
        for i in range(1,len(salary)-1):
            x+=salary[i]
        return x/y
            
        
