class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        x=Counter(nums)
        list1=[]
        for i,v in x.items():
            list1.append([v,i])
        list1.sort(key=lambda x: (x[0], -x[1]))
        list2=[]
        for i in list1:
            list2.extend([i[1]]*i[0])
        return list2
