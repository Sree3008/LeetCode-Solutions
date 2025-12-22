class Solution:
    def sortVowels(self, s: str) -> str:
        list1=[]
        list2=[]
        v='AEIOUaeiou'
        for i in s:
            if i in v:
                list1.append(ord(i))
        list1.sort()
        list1.reverse()
        for i in s:
            if i in v:
                x=list1.pop()
                list2.append(chr(x))
            else:
                list2.append(i)
        st=''
        for i in list2:
            st+=i
        print(st)
        return st

        
