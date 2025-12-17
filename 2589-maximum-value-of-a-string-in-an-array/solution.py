class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        list1=[]
        for i in strs:
            if i.isdigit():
                list1.append(int(i))
            else:
                x=len(i)
                list1.append(x)
        print(list1)
        return max(list1)
