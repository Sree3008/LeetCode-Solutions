class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness(n):
            s=str(n)
            if len(s)<3:
                return 0
            w=0
            for i in range(1,len(s)-1):
                left=int(s[i-1])
                mid=int(s[i])
                right=int(s[i+1])

                if mid>left and mid>right:
                    w=w+1
                elif mid<left and mid<right:
                    w=w+1
            return w
        total=0
        for x in range(num1,num2+1):
            total=total+waviness(x)
        return total
      
        
