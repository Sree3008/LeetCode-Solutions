class Solution:
    def reverseWords(self, s: str) -> str:
        list1=s.split()
        vow='aeiou'
        list2=[]
        for i in list1:
            c=0
            for j in i:
                if j in vow:
                    c+=1
            list2.append(c)
        x=list2[0]
        list3=[list1[0]]
        for i in range(1,len(list1)):
            if list2[i]==x:
                list3.append(list1[i][::-1])
            else:
                list3.append(list1[i])
        
        return ' '.join(list3)
                
        
