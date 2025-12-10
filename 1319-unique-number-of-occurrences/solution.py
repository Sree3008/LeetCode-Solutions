class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        list1=[]
        set1=set(arr)
        for i in set1:
                list1.append(arr.count(i))
        if len(list1)==len(set(list1)):
            return True
        return False
