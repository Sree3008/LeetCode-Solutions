class Solution:
    def busyStudent(self, s: List[int], e: List[int], queryTime: int) -> int:
        c=0
        for i,v in zip(s,e):
            if i<=queryTime<=v:
                c+=1
        return c
