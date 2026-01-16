class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        list1=[]
        for i in tokens:
            if i.lstrip('-').isdigit():
                list1.append(int(i))
            else:
                x=list1.pop()
                y=list1.pop()
                if i=='+':
                    list1.append(x+y)
                elif i=='-':
                    list1.append(y-x)
                elif i=='*':
                    list1.append(y*x)
                else:
                    list1.append(int(y/x))
        return list1[0]
