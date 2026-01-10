class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        x=Counter()
        list1=[]
        for i in range(len(nums)-1):
            if nums[i]==key:
                x[nums[i+1]] += 1 
                list1.append(nums[i+1])
        list2=[]
        for i,v in x.items():
            if i in list1:
                list2.append([i,v])
        list2.sort(key=lambda item: item[1],reverse=True)
        print(list2)
        if list2:
            return list2[0][0]
        return -1

            

