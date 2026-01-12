class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        x=["electronics", "grocery", "pharmacy", "restaurant"]
        list1=[]
        for i in range(len(code)): 
            if code[i] and (code[i] == "_" or code[i].replace('_', '').isalnum()):
                if businessLine[i] in x:
                    if isActive[i]==True: 
                        list1.append((x.index(businessLine[i]),code[i])) 
        list1.sort()
        return [c for _,c in list1]
  
