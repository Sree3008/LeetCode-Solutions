class Solution:
    def fizzBuzz(self, m: int) -> List[str]:
        list1=[]
        for n in range(1, m + 1):
            if n%3==0 and n%5==0:
                list1.append('FizzBuzz')
            elif n%3==0:
                list1.append('Fizz')
            elif n%5==0:
                list1.append('Buzz')
            else:
                list1.append(str(n))
        return list1
