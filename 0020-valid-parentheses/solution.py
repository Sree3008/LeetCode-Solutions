class Solution:
    def isValid(self, s: str) -> bool:
        list1=[]
        for i in s:
            if i=='(' or i=='[' or i=='{':
                list1.append(i)
            elif i==')' or i==']' or i=='}':
                if not list1:
                    return False
                x=list1.pop()
                if (x=='(' and i!=')') or (x=='[' and i!=']') or (x=='{' and i!='}'):
                        return False
        return len(list1)==0
