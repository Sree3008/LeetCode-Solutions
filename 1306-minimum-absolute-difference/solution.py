class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        list2=[]
        arr.sort()
        mini=float('inf')
        for i in range(len(arr)-1):
            x=arr[i+1]-arr[i]
            if x<mini:
                mini=x
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]==mini:
                list2.append([arr[i],arr[i+1]])
                
        return list2

