class Solution:
    def makeGood(self, s: str) -> str:
        list1=list(s)
        list2=[]
        for i in range(0,len(list1)):
            if list2:
                if list2[-1].isupper() and list1[i].islower() and list2[-1].lower() == list1[i]:
                        list2.pop()
                        continue
                elif list2[-1].islower() and list1[i].isupper() and list2[-1] == list1[i].lower():
                        list2.pop()
                        continue
            list2.append(list1[i])
        
        return ''.join(list2)
        

                
        
