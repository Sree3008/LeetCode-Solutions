class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        if s==goal:
            return len(set(s))<len(s)
        list1=[]
        for i in range(len(s)):
            if s[i]!=goal[i]:
                list1.append(i)
        if len(list1)!=2:
            return False
        i,j=list1
        return s[i]==goal[j] and s[j]==goal[i]        
