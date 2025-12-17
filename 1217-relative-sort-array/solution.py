class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        x=Counter(arr1)
        s=[i for i in arr1 if i not in arr2]
        s.sort()
        list1=[]
        for i in arr2:
            if i in x.keys():
                h=x[i]
                list1.extend([i]*h)
        list1.extend(s)
        
        return list1
