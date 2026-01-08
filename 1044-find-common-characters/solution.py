class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # x=Counter(words[0])
        # y=Counter(words[1])
        # common = x&y
        # z=Counter(words[2])
        # res=common&z
        # list1=[]
        # for i,v in res.items():
        #     t=[i]*v
        #     list1.extend(t)
        # return list1
        c=Counter(words[0])
        for i in words[1:]:
            c&=Counter(i)
        return list(c.elements())  
        
        
        
