class Solution:
    def countTriples(self, n: int) -> int:
        c=0
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                for k in range(j+1,n+1):
                    if i*i+j*j==k*k:
                        c+=2
        return c
