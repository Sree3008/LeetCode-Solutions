class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        list1=[]
        for i in letters:
            x=ord(i)
            list1.append(x)
        y=ord(target)
        for i in list1:
            if i>y:
                z=chr(i)
                return z
        return letters[0]
        
