class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        list1=[0]*len(arr)
        maxi=-1
        for i in range(len(arr) - 1, -1, -1):
            list1[i]=maxi
            if maxi<arr[i]:
                maxi=arr[i]
        print(list1)
        return list1


        
