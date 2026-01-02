class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        list1=[]
        for i in range(left,right+1):
            n=i
            c=1
            while n > 0:
                x = n % 10
                if x==0 or i%x!= 0:
                    c = 0
                    break
                n //= 10
            if c==1: 
                list1.append(i)
        print(list1)
        return list1

