class Solution:
    def clearDigits(self, s: str) -> str:
        list1=list(s)
        i=0
        while i<len(list1):
            if list1[i].isdigit():
                list1.pop(i)
                if i-1>=0:
                    list1.pop(i-1)
                    i-=1
            else:
                i+=1
        return ''.join(list1)

        
