class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        res={'type':0,'color':1,'name':2}
        res1=res[ruleKey]
        c=0
        for i in items:
            if i[res1]==ruleValue: 
                c+=1
        return c
        
