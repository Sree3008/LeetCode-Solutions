class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        list1=list(map(int,nums))
        list1.sort(reverse='True')
        return str(list1[k-1])

