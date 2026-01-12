class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        list2=sorted(score,reverse=True)
        
        s1=list2[0] if len(list2)>0 else None
        s2=list2[1] if len(list2)>1 else None
        s3=list2[2] if len(list2)>2 else None
        list1=[]
        list3=[]
        for i in score:                       
            list1.append(i)
        print(list1)
        for i in list1:
            if i==s1:
                list3.append("Gold Medal")
            elif i==s2:
                list3.append("Silver Medal")
            elif i==s3:
                list3.append("Bronze Medal")
            else:
                list3.append(str(list2.index(i)+1))
        return list3 
        


            
