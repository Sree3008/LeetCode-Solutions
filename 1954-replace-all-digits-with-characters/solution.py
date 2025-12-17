class Solution:
    def replaceDigits(self, s: str) -> str:
        list1=list(s)
        r=list1[0]
        for i in range(1,len(list1)):
            if list1[i].isdigit():
                x=list1[i-1]
                a=int(list1[i])
                y=ord(x)+a
                z=chr(y)
                r+=z
            else:
                r+=list1[i]
        print(s)
        return r

        
