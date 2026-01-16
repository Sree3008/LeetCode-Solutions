class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temp)
        for i in range(len(temp)):
            while stack and temp[i]>temp[stack[-1]]:
                x=stack.pop() 
                res[x]=i-x
            stack.append(i)
        return res
            
        
