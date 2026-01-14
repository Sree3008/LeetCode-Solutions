class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        c0=students.count(0)
        c1=students.count(1)
        for i in sandwiches:
            if i==0 and c0>0:
                c0-=1 
            elif i==1 and c1>0:
                c1-=1
            else:
                break
        return c0+c1
