class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        list1=s.split()
        list2=[int(i) for i in list1 if i.isdigit()]
        for i in range(len(list2)-1):
            if(list2[i]<list2[i+1]):
                continue
            else:
                return False
        return True
